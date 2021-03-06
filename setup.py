import os, re

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

try:
    import slack_logging_handler.__version__ as version
except ImportError:
    # If we get an import error, find the version string manually
    version = "unknown"
    with open(os.path.join(here, 'slack_logging_handler', '__init__.py')) as f:
        for line in f:
            match = re.search('__version__ *= *[\'"](?P<version>.+)[\'"]', line)
            if match:
                version = match.group('version')
                break

with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

requires = [
    'requests',
]

if __name__ == "__main__":
    setup(
        name = 'slack-logging-handler',
        version = version,
        description = 'Python logging handler that posts to a Slack channel using a webhook',
        long_description = README,
        classifiers = [
            "Programming Language :: Python",
        ],
        author = 'Matt Pryor',
        author_email = 'matt.pryor@stfc.ac.uk',
        url = 'https://github.com/cedadev/slack-logging-handler',
        keywords = 'logging slack',
        packages = find_packages(),
        include_package_data = True,
        zip_safe = False,
        install_requires = requires,
    )
