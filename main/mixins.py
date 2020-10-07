from rest_framework import generics, permissions, viewsets


class MixedPermissionModelViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {}

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]