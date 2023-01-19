from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ViewSet

from pulpcore.app.response import OperationPostponedResponse
from pulpcore.app.serializers import AsyncOperationResponseSerializer, OrphansCleanupSerializer
from pulpcore.app.tasks import orphan_cleanup
from pulpcore.tasking.tasks import dispatch


class OrphansCleanupViewset(ViewSet):
    serializer_class = OrphansCleanupSerializer

    @extend_schema(
        description="Trigger an asynchronous orphan cleanup operation.",
        responses={202: AsyncOperationResponseSerializer},
    )
    def cleanup(self, request):
        """
        Triggers an asynchronous orphan cleanup operation.
        """
        task = orphan_cleanup.dispatch(request.data)
        return OperationPostponedResponse(task, request)
