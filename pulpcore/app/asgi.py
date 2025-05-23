"""
ASGI config for pulp project.
"""

from django.core.asgi import get_asgi_application

from pulpcore.app.entrypoint import using_pulp_api_worker

if not using_pulp_api_worker.get(False):
    raise RuntimeError("This app must be executed using pulpcore-api entrypoint.")

application = get_asgi_application()
