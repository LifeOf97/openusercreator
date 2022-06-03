from rest_framework.metadata import BaseMetadata


class AppMetadata(BaseMetadata):
    def determine_metadata(self, request, view):
        return {
            'name': "Openuserdata Creators API View",
            'description': "REST API used by the Openuserdata creators.",            
        }