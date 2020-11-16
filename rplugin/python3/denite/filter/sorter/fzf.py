import os

from subprocess import Popen, DEVNULL, PIPE

from denite.base.filter import Base
from denite.util import error


class Filter(Base):
    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'sorter/fzf'
        self.description = 'fzf sorter'

        self.__disabled = False

    def filter(self, context):
        if not context['candidates'] or not context['input'] or \
                self.__disabled:
            return context['candidates']

        if self.__disabled:
            return []

        fzf = '.exe' if context['is_windows'] else ''
        fzf = 'fzf' + fzf

        result = self._get_result(
            fzf,
            context['candidates'],
            context['encoding'],
            context['input'],
        )

        d = {x['word']: x for x in context['candidates']}
        return [d[word] for word in result.split('\n') if word in d] + \
               [x for x in context['candidates'] if x['word'] not in result]

    def _get_result(self, fzf, candidates, encoding, pattern):
        arg = [fzf, '-f', pattern]

        try:
            p = Popen(
                arg,
                stdin=PIPE,
                stdout=PIPE,
                stderr=DEVNULL,
            )
        except OSError as e:
            if e.errno == os.errno.ENOENT:
                message = f'{fzf} is not properly installed.'
                self._throw_error(message)
                self.__disabled = True
            else:
                message = f'{fzf} could not be executed.'
                self._throw_error(message)

        stdout, _ = p.communicate('\n'.join([d['word'] for d in candidates]).encode(encoding))

        # If fzf does not find a match, it will return 1.
        if p.returncode not in [0, 1]:
            message = f'{fzf} exited with code {p.returncode}.'
            self._throw_error(message)

        return stdout.decode(encoding)

    def _throw_error(self, message):
        message = f'{self.name}: {message}'
        error(self.vim, message)
