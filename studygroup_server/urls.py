from django.conf.urls import patterns, url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import routers
from server import views

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/?', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^verify_credentials/?', 'rest_framework.authtoken.views.obtain_auth_token'),
    url(r'^courses/add/?', views.AddCourseView.as_view()), 
    url(r'^courses/remove/?', views.RemoveCourseView.as_view()),
    url(r'^courses/filter/?', views.FilterCourseView.as_view()), 
    url(r'^register/?', views.RegisterUserView.as_view()),     
    url(r'^users/update_profile/?', views.UpdateProfileView.as_view()),    
    url(r'^courses/university/(?P<universityID>.+)/?$', views.CourseList.as_view()),    
    url(r'^universities/list/?', views.UniversityView.as_view()),
    url(r'^locations/university/(?P<universityID>.+)/?$', views.UniversityLocationsView.as_view()),     
    url(r'^users/profile/?', views.StudentProfileView.as_view()),
    url(r'^sessions/courses/', views.SessionPerCourseView.as_view()),
    url(r'^sessions/host', views.SessionHostingView.as_view()),
    url(r'^sessions/attend', views.SessionAttendingView.as_view()),    
    url(r'^sessions/join/?', views.SessionJoinView.as_view()),
    url(r'^sessions/leave/?', views.SessionLeaveView.as_view()),
    url(r'^sessions/create/?$', views.SessionCreateView.as_view()),
    url(r'^sessions/edit/?$', views.SessionUpdateView.as_view()),

    url(r'^sessions/university/(?P<universityID>.+)/?$', views.SessionByUniversityView.as_view()),
    url(r'^xmpp/$',views.XMPPView.as_view()),
)

urlpatterns += staticfiles_urlpatterns()
