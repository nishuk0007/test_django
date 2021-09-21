from test_app.models import User
from rest_framework import generics
from rest_framework.response import Response
from test_app.serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet
# from test_app.paginations import CustomPagination


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UpdateMultipleUsersActiveStatusView(generics.UpdateAPIView):
    queryset = User.objects.all()

    def patch(self, request, *args, **kwargs):
        active_status = request.data.get("is_active")
        ids = request.data.get("ids")
        try:
            ids = ids.split(",")
        except:
            ids = [ids]
        qss = self.queryset.filter(id__in=ids)
        if qss:
            try:
                if active_status == 'active':
                    for qs in qss:
                        qs.is_active = True
                        qs.save()
                    return Response({"status": "OK"})
                else:
                    for qs in qss:
                        qs.is_active = False
                        qs.save()
                    return Response({"status": "OK"})
            except Exception as e:
                print(e)
        else:
            return Response({"status": "Record not found"})


class DeleteMultipleUsersView(generics.DestroyAPIView):
    queryset = User.objects.all()

    def delete(self, request, *args, **kwargs):
        ids = request.data.get("ids")
        try:
            ids = ids.split(",")
        except:
            ids = [ids]
        qss = self.queryset.filter(id__in=ids)
        if qss:
            try:
                for qs in qss:
                    qs.delete()
                return Response({"status": "OK"})
            except Exception as e:
                print(e)
        else:
            return Response({"status": "Record not found"})
