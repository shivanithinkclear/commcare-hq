from django.conf.urls import *

from corehq.apps.domain.utils import grandfathered_domain_re
from .views import (
    DefaultProjectUserSettingsView, DomainRequestView, EditWebUserView,
    ListWebUsersView, InviteWebUserView, change_password,
    domain_accounts, delete_phone_number, make_phone_number_default, verify_phone_number, add_domain_membership,
    remove_web_user, undo_remove_web_user, delete_invitation, reinvite_web_user, delete_request,
    location_restriction_for_users, accept_invitation, post_user_role, delete_user_role, register_fcm_device_token,
    test_httpdigest)
from .views.mobile.custom_data_fields import UserFieldsView
from .views.mobile.groups import (GroupsListView, EditGroupMembersView,
    BulkSMSVerificationView)
from .views.mobile.users import (
    UploadCommCareUsers, EditCommCareUserView,
    ConfirmBillingAccountForExtraUsersView, UserUploadStatusView,
    CommCareUserSelfRegistrationView, MobileWorkerListView,
    CreateCommCareUserModal, DemoRestoreStatusView,
    update_user_data, update_user_groups, archive_commcare_user, delete_commcare_user, restore_commcare_user,
    toggle_demo_mode, reset_demo_user_restore, demo_restore_job_poll, user_upload_job_poll,
    download_commcare_users, set_commcare_user_group)


urlpatterns = patterns('corehq.apps.users.views',
    url(r'^$', DefaultProjectUserSettingsView.as_view(), name=DefaultProjectUserSettingsView.urlname),
    url(r'^change_password/(?P<login_id>[ \w-]+)/$', change_password, name="change_password"),
    url(r'^domain_accounts/(?P<couch_user_id>[ \w-]+)/$', domain_accounts, name='domain_accounts'),
    url(r'^delete_phone_number/(?P<couch_user_id>[ \w-]+)/$',
        delete_phone_number,
        name='delete_phone_number'),
    url(r'^make_phone_number_default/(?P<couch_user_id>[ \w-]+)/$',
        make_phone_number_default,
        name='make_phone_number_default'),
    url(r'^verify_phone_number/(?P<couch_user_id>[ \w-]+)/$',
        verify_phone_number,
        name='verify_phone_number'),
    url(r'^add_domain_membership/(?P<couch_user_id>[ \w-]+)/(?P<domain_name>%s)/$' % grandfathered_domain_re,
        add_domain_membership,
        name='add_domain_membership'),
    url(r'^web/account/(?P<couch_user_id>[ \w-]+)/$', EditWebUserView.as_view(), name=EditWebUserView.urlname),
    url(r'^web/remove/(?P<couch_user_id>[ \w-]+)/$', remove_web_user, name='remove_web_user'),
    url(r'^web/undo_remove/(?P<record_id>[ \w-]+)/$', undo_remove_web_user, name='undo_remove_web_user'),
    url(r'^web/invite/$', InviteWebUserView.as_view(), name=InviteWebUserView.urlname),
    url(r'^web/reinvite/$', reinvite_web_user, name='reinvite_web_user'),
    url(r'^web/request/$', DomainRequestView.as_view(), name=DomainRequestView.urlname),
    url(r'^web/delete_invitation/$', delete_invitation, name='delete_invitation'),
    url(r'^web/delete_request/$', delete_request, name='delete_request'),
    url(r'^web/location_restriction_for_users/$', location_restriction_for_users, name='location_restriction_for_users'),
    url(r'^web/$', ListWebUsersView.as_view(), name=ListWebUsersView.urlname),
    url(r'^join/(?P<invitation_id>[ \w-]+)/$', accept_invitation, name='domain_accept_invitation'),
    url(r'^web/role/save/$', post_user_role, name='post_user_role'),
    url(r'^web/role/delete/$', delete_user_role, name='delete_user_role'),
    url(r'^register_fcm_device_token/(?P<couch_user_id>[ \w-]+)/(?P<device_token>[ \w-]+)/$',
        register_fcm_device_token, name='register_fcm_device_token'),
    url(r'^httpdigest/?$', test_httpdigest, name='test_httpdigest'),
) + \
patterns("corehq.apps.users.views.mobile.users",
    url(r'^commcare/$',
        MobileWorkerListView.as_view(),
        name=MobileWorkerListView.urlname),
    url(r'^commcare/fields/$', UserFieldsView.as_view(), name=UserFieldsView.urlname),
    url(r'^commcare/account/(?P<couch_user_id>[ \w-]+)/$', EditCommCareUserView.as_view(),
        name=EditCommCareUserView.urlname),
    url(r'^commcare/account/(?P<couch_user_id>[ \w-]+)/user_data/$', update_user_data, name='update_user_data'),
    url(r'^commcare/account/(?P<couch_user_id>[ \w-]+)/groups/$', update_user_groups, name='update_user_groups'),
    url(r'^commcare/archive/(?P<user_id>[ \w-]+)/$', archive_commcare_user, name='archive_commcare_user'),
    url(r'^commcare/unarchive/(?P<user_id>[ \w-]+)/$', archive_commcare_user,
        name='unarchive_commcare_user', kwargs={'is_active': True}),
    url(r'^commcare/delete/(?P<user_id>[ \w-]+)/$', delete_commcare_user, name='delete_commcare_user'),
    url(r'^commcare/restore/(?P<user_id>[ \w-]+)/$', restore_commcare_user, name='restore_commcare_user'),
    url(r'^commcare/toggle_demo_mode/(?P<user_id>[ \w-]+)/$', toggle_demo_mode, name='toggle_demo_mode'),
    url(r'^commcare/reset_demo_user_restore/(?P<user_id>[ \w-]+)/$', reset_demo_user_restore,
        name='reset_demo_user_restore'),
    url(r'^commcare/demo_restore/status/(?P<download_id>[0-9a-fA-Z]{25,32})/(?P<user_id>[ \w-]+)/$',
        DemoRestoreStatusView.as_view(),
        name=DemoRestoreStatusView.urlname),
    url(r'^commcare/demo_restore/poll/(?P<download_id>[0-9a-fA-Z]{25,32})/$', demo_restore_job_poll,
        name='demo_restore_job_poll'),
    url(r'^commcare/upload/$', UploadCommCareUsers.as_view(), name=UploadCommCareUsers.urlname),
    url(r'^commcare/upload/status/(?P<download_id>[0-9a-fA-Z]{25,32})/$', UserUploadStatusView.as_view(),
        name=UserUploadStatusView.urlname),
    url(r'^commcare/upload/poll/(?P<download_id>[0-9a-fA-Z]{25,32})/$',
        user_upload_job_poll, name='user_upload_job_poll'),
    url(r'^commcare/download/$', download_commcare_users, name='download_commcare_users'),
    url(r'^commcare/set_group/$', set_commcare_user_group, name='set_commcare_user_group'),
    url(r'^commcare/new_mobile_worker_modal/$',
        CreateCommCareUserModal.as_view(),
        name=CreateCommCareUserModal.urlname),
    url(r'^commcare/confirm_charges/$', ConfirmBillingAccountForExtraUsersView.as_view(),
        name=ConfirmBillingAccountForExtraUsersView.urlname),
    url(r'^commcare/register/(?P<token>[\w-]+)/$', CommCareUserSelfRegistrationView.as_view(),
        name=CommCareUserSelfRegistrationView.urlname),
) +\
patterns("corehq.apps.users.views.mobile.groups",
    url(r'^groups/$', GroupsListView.as_view(), name=GroupsListView.urlname),
    url(r'^groups/(?P<group_id>[ \w-]+)/$', EditGroupMembersView.as_view(), name=EditGroupMembersView.urlname),
    url(r'^groups/sms_verification/(?P<group_id>[ \w-]+)$', BulkSMSVerificationView.as_view(),
        name=BulkSMSVerificationView.urlname),
)
