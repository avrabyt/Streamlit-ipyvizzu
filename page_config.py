from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
from time import sleep
from typing import Any, Dict, List, Optional

import streamlit as st
import yaml
from streamlit import StreamlitAPIException, _get_script_run_ctx
from streamlit.source_util import get_pages
from streamlit.util import calc_md5


@dataclass
class Config:
    page_name: str
    icon: str
    visible: Optional[bool] = True
    date_added: Optional[date] = None
    layout: Optional[str] = "centered"
    is_section: Optional[bool] = False
    is_nested: Optional[bool] = True
    script_path: Optional[str] = None

    def get_script_path(self) -> str:
        if self.script_path is not None:
            return self.script_path

        if self.is_section:
            return "streamlit_app.py"

        if self.standard_page_name.lower() == "streamlit_app":
            return "streamlit_app.py"

        return f"pages/{self.standard_page_name.lower()}.py"

    @property
    def standard_page_name(self) -> str:
        return self.page_name.replace(" ", "_")

    @property
    def is_new(self) -> bool:
        return (
            self.date_added is not None
            and self.date_added > date.today() - timedelta(days=30)
        )

    @property
    def page_hash(self) -> str:
        abs_path = Path(self.get_script_path())
        key = calc_md5(str(abs_path))
        if self.is_section:
            key += self.page_name

        return key

    def as_dict(self) -> Dict[str, str]:
        return {
            "page_script_hash": self.page_hash,
            "page_name": self.standard_page_name,
            "icon": self.icon,
            "script_path": self.get_script_path(),
        }


PageList = List[Dict[str, Any]]


def get_config_file() -> Dict[str, List[Dict[str, Any]]]:
    sections = yaml.safe_load(Path("page_config.yaml").read_text())
    return sections


def get_page_config() -> List[Config]:
    """
    Returns a dictionary of page configs.
    """
    # return yaml.safe_load(Path("page_config.yaml").read_text())["pages"]
    config = get_config_file()
    other_pages = config["pages"]
    sections = config["sections"]
    pages: List[Dict[str, Any]] = []

    for page in other_pages:
        pages.append({**page, "is_section": False, "is_nested": False})

    for section in sections:
        pages.append(
            {
                "page_name": section["name"],
                "icon": section["icon"],
                "is_section": True,
            }
        )
        for page in section["pages"]:
            pages.append(page)

    # Drop any pages that are set to not visible
    configs = [Config(**p) for p in pages if p.get("visible", True)]

    return configs


def get_page_name_from_hash(page_hash: str) -> str:
    return get_all_pages()[page_hash]["page_name"]


def get_current_page_config() -> Config:
    page_config_overrides = get_page_config()
    page_name = get_page_name()

    for page in page_config_overrides:
        if page.standard_page_name == page_name:
            return page

    raise KeyError


def overwrite_page_config():
    """
    Replace the official streamlit pages config values by whatever is in
    page_config.yaml
    """
    if st.session_state.get("updated_config", False) is True:
        return

    page_config_overrides = get_page_config()

    page_config_overrides_by_name = {
        page.standard_page_name: page for page in page_config_overrides
    }

    # Get the page list dictionary from native streamlit (streamlit_app.py + pages/*.py)
    page_config = get_all_pages()

    # Empty the current page list
    for page in list(page_config):
        page_config.pop(page)

    # Populate the page list with the pages defined in page_config.yaml
    for page, config in page_config_overrides_by_name.items():
        page_config[config.page_hash] = config.as_dict()

    st.session_state["updated_config"] = True

    sleep(0.1)

    st.experimental_rerun()


def add_styling():
    page_config = get_page_config()

    styling = ""

    idx = 1
    for page in page_config:
        if page.is_new:
            styling += f"""

            li:nth-child({idx}) span:nth-child(2)::after {{
                content: "🆕"; /* Add New icon to the end of the page name */
                padding-left: 0.5rem;
            }}
            """

        if page.is_section:
            styling += f"""
                li:nth-child({idx}) a {{
                    pointer-events: none; /* Disable clicking on section header */
                }}
            """
        elif page.is_nested:
            # Unless specifically unnested, indent all pages that aren't section headers
            styling += f"""
                li:nth-child({idx}) span:nth-child(1) {{
                    margin-left: 1.5rem;
                }}
            """

        idx += 1

    st.write(
        f"""
        <style>
            {styling}
        </style>
        """,
        unsafe_allow_html=True,
    )


def get_all_pages() -> Dict[str, Dict[str, str]]:
    """
    Returns a dictionary of dictionaries, of the form
    {
        "<page_hash>": {
            {
                'page_script_hash': "<page_hash>",
                'page_name': '<page_name_with_underscores>',
                'icon': '<icon>',
                'script_path': '<page_file_path>'}
        }
    }
    """
    return get_pages("streamlit_app.py")


def get_page_name() -> str:
    ctx = _get_script_run_ctx()

    if ctx is None:
        raise TypeError("Only works when run from a streamlit app")

    page_hash = ctx.page_script_hash

    return get_page_name_from_hash(page_hash)


def add_page_header():
    page_config = get_current_page_config()

    title = page_config.page_name

    if page_config.is_new:
        title = f"**NEW!** {title}"

    try:
        st.set_page_config(
            page_title=title,
            page_icon=page_config.icon,
            layout=page_config.layout,
        )
    except StreamlitAPIException:
        pass

    st.title(f"{page_config.icon} {title}")


def standard_page_widgets():
    overwrite_page_config()
    add_page_header()
    add_styling()