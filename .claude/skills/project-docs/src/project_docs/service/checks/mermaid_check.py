from __future__ import annotations

# Standard library imports
from logging import Logger
from typing import ClassVar, List, Optional

# First-party imports
from harness_core.markdown.markdown_text import MarkdownText
from project_docs.service.checks.document_check import DocumentCheck
from project_docs.storage.files.document_files import DocumentFiles
from project_docs.storage.mermaid.mermaid_renderer import MermaidRenderer


class MermaidCheck(DocumentCheck):
    """Checks that every Mermaid block of the documentation renders.

    Attributes:
        LANGUAGE (str): The language of the blocks checked.
        renderer (MermaidRenderer): Renders one block with ``mmdc``.

    Notes:
        **Without ``mmdc`` on the ``PATH`` nothing is printed**, so that ``check`` stays silent on a complete
        documentation, and a ``WARNING`` in the log says the blocks were not rendered.
    """

    LANGUAGE: ClassVar[str] = "mermaid"

    def __init__(self, files: DocumentFiles, renderer: MermaidRenderer, logger: Optional[Logger] = None) -> None:
        """Set the files and the renderer.

        Args:
            files (DocumentFiles): The documentation's files.
            renderer (MermaidRenderer): Renders one block with ``mmdc``.
            logger (Optional[Logger]): Logger instance.
        """
        super().__init__(files, logger)
        self.renderer = renderer

    ############################
    # Publicly Exposed Methods #
    ############################

    def problems(self) -> List[str]:
        """List the Mermaid blocks that do not render.

        Returns:
            List[str]: One line per block, with its document and the line of its opening fence.
        """
        if not self.renderer.available():
            self.logger.warning("mmdc is not on the PATH: the Mermaid blocks were not rendered.")
            return []
        problems: List[str] = []
        blocks = 0
        for document in self.files.documents():
            for line, source in MarkdownText.fenced_blocks(self.files.read(document), self.LANGUAGE):
                blocks += 1
                error = self.renderer.render(source)
                if error is not None:
                    problems.append(f"{document}:{line}: Mermaid block does not render: {error}")
        self.logger.info("Rendered %d Mermaid blocks, %d failed.", blocks, len(problems))
        return problems
