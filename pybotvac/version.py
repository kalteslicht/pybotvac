from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # During type checking, we assume the standard library interface is available
    from importlib.metadata import PackageNotFoundError, version
else:
    # At runtime, use stdlib importlib.metadata if available, otherwise fall back
    try:
        from importlib.metadata import PackageNotFoundError, version
    except ImportError:
        try:
            from importlib_metadata import PackageNotFoundError, version  # backport
        except ImportError:
            # Final fallback: provide minimal stubs
            class PackageNotFoundError(Exception):
                """Fallback exception used when metadata backends are unavailable."""
                pass

            def version(_dist_name: str) -> str:
                """Fallback version() that always raises PackageNotFoundError."""
                raise PackageNotFoundError(f"Package '{_dist_name}' not found")


try:
    __version__ = version("pybotvac")
except PackageNotFoundError:  # pragma: no cover - environment dependent
    __version__ = "unknown"
