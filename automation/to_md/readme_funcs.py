"""Scripts related to readme
"""

##########
# Imports
##########

import logging
from typing import Optional, Tuple

import aux_funcs
import constants


##########
# ToC function
##########

def write_toc_link(file_name: str) -> None:
    """Writes link to return to ToC to in_file."""
    logging.debug(f"IN-file - {file_name}")
    TOC_INFO = """<b><a href="{}">:arrow_up: Table of Contents</a></b>
<br/>
<br/>
""".format(constants.TOC_HEADER)

    with open(file_name.resolve(), 'a') as in_file:
        in_file.write('\n' * 2)
        in_file.write(TOC_INFO)
        in_file.write('\n' * 2)
    return


##########
# Table of contents file
##########

def write_to_toc_file(domain_dir: str, level: int, toc_file: str) -> None:
    """Writes header at assigned level to markdown table of contents file.

    Args:
        domain_dir (str): Header to write
        level (int): level of header
    """
    header_format = "[{}](#{})"
    
    dirname = aux_funcs.get_dirname(domain_dir)
    if dirname not in constants.number_dirs:
        logging.debug(f"Removing preceeding numbers from {dirname}")
        sub_dir = dirname[dirname.find('_') + 1:]
    else:
        logging.debug(f"{dirname} in constants.number_dirs")
        sub_dir = dirname

    header  = sub_dir.replace('_', ' ').title()
    doc_link = sub_dir.lower()

    ## Replace ToC contents based on format
    if doc_link in constants.number_dirs:
        doc_link = doc_link.replace('-', '_')
    else:
        doc_link = doc_link.replace('_', '-')


    logging.debug(header + doc_link)
    with open(toc_file, 'a') as infile:
        formatted_header = " ".join([
            " " * 4 * (level - 1),
            '-',
            header_format.format(header, doc_link),
            "\n"
        ])
        logging.debug(f"Writing header to ToC file: {formatted_header}")
        infile.write(formatted_header)
    return



##########
# Readme names
##########
def get_readme_names(dir_name: str,) -> Tuple[str, str]:
    """Returns tuple representing pre-readme & readme filenames.

    Args:
        dir_name (str): directory to search in

    Returns:
        Tuple[str, str]: pre_readme and readme filenames.
    """
    logging.debug(f"DIR - {dir_name}")
    filename_pre_readme = dir_name / constants.PRE_README_FILENAME
    filename_readme = dir_name / constants.README_FILENAME

    logging.debug(f"DIR - created {filename_pre_readme}, {filename_readme}")
    return (filename_pre_readme, filename_readme)


def get_readme_helper_filenames(home_dir) -> str:
    """Returns tuple representing pre-readme & readme filenames.

    Args:
        dir_name (str): directory to search in

    Returns:
        (str) filename for readme contents
    """
    logging.debug(f"DIR - {home_dir}")
    filename_readme_contents = home_dir / constants.README_CONTENTS_FILENAME
    filename_readme_toc = home_dir / constants.TOC_FILENAME

    logging.debug(f"DIR - created {filename_readme_contents}, {filename_readme_toc}")
    return (filename_readme_contents, filename_readme_toc)



def create_file(filename: str, header: Optional[str] = None, level: int = 2) -> None:
    """Creates table of contents support file."""
    logging.info(f"Creating file {filename}")
    with open(filename, 'w') as infile:
        if header:
            formatted_header = ' '.join(['\n', '#' * level, header])
            infile.write(formatted_header)
        infile.write('\n')
        return



##########
# Write readme to readme
##########

def write_in_to_out_file(in_file: str, out_file: str) -> None:
    """Writes contents from one file to another file.

    Args:
        in_file (str): file to read contents from
        out_file (str): file to write contents from
    """
    logging.debug(f"Files - in: {in_file}, out: {out_file}")
    with open(out_file, 'a') as outfile:
        # outfile.write(constants.LINE_BREAK)
        outfile.write('\n')

        with open(in_file, 'r') as in_file:
            for line in in_file:
                outfile.write(line)
    return


def write_newline(filename) -> None:
    with open(filename, 'a') as infile:
        infile.write('\n')
    return
