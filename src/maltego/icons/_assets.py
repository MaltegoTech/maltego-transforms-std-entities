from importlib.resources import files


def icon_path(*parts: str) -> str:
    return str(files("maltego.icons").joinpath("assets", *parts))
