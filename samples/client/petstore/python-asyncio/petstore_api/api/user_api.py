# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    OpenAPI spec version: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from petstore_api.api_client import ApiClient


class UserApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_user(self, user, **kwargs):  # noqa: E501
        """Create user  # noqa: E501

        This can only be done by the logged in user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_user(user, async=True)
        >>> result = thread.get()

        :param async bool
        :param User user: Created user object (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_user_with_http_info(user, **kwargs)  # noqa: E501
        else:
            (data) = self.create_user_with_http_info(user, **kwargs)  # noqa: E501
            return data

    def create_user_with_http_info(self, user, **kwargs):  # noqa: E501
        """Create user  # noqa: E501

        This can only be done by the logged in user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_user_with_http_info(user, async=True)
        >>> result = thread.get()

        :param async bool
        :param User user: Created user object (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['user']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_user" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'user' is set
        if ('user' not in local_var_params or
                local_var_params['user'] is None):
            raise ValueError("Missing the required parameter `user` when calling `create_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'user' in local_var_params:
            body_params = local_var_params['user']
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/user', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=local_var_params.get('async'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_users_with_array_input(self, user, **kwargs):  # noqa: E501
        """Creates list of users with given input array  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_users_with_array_input(user, async=True)
        >>> result = thread.get()

        :param async bool
        :param list[User] user: List of user object (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_users_with_array_input_with_http_info(user, **kwargs)  # noqa: E501
        else:
            (data) = self.create_users_with_array_input_with_http_info(user, **kwargs)  # noqa: E501
            return data

    def create_users_with_array_input_with_http_info(self, user, **kwargs):  # noqa: E501
        """Creates list of users with given input array  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_users_with_array_input_with_http_info(user, async=True)
        >>> result = thread.get()

        :param async bool
        :param list[User] user: List of user object (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['user']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_users_with_array_input" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'user' is set
        if ('user' not in local_var_params or
                local_var_params['user'] is None):
            raise ValueError("Missing the required parameter `user` when calling `create_users_with_array_input`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'user' in local_var_params:
            body_params = local_var_params['user']
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/user/createWithArray', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=local_var_params.get('async'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_users_with_list_input(self, user, **kwargs):  # noqa: E501
        """Creates list of users with given input array  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_users_with_list_input(user, async=True)
        >>> result = thread.get()

        :param async bool
        :param list[User] user: List of user object (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_users_with_list_input_with_http_info(user, **kwargs)  # noqa: E501
        else:
            (data) = self.create_users_with_list_input_with_http_info(user, **kwargs)  # noqa: E501
            return data

    def create_users_with_list_input_with_http_info(self, user, **kwargs):  # noqa: E501
        """Creates list of users with given input array  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_users_with_list_input_with_http_info(user, async=True)
        >>> result = thread.get()

        :param async bool
        :param list[User] user: List of user object (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['user']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_users_with_list_input" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'user' is set
        if ('user' not in local_var_params or
                local_var_params['user'] is None):
            raise ValueError("Missing the required parameter `user` when calling `create_users_with_list_input`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'user' in local_var_params:
            body_params = local_var_params['user']
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/user/createWithList', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=local_var_params.get('async'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_user(self, username, **kwargs):  # noqa: E501
        """Delete user  # noqa: E501

        This can only be done by the logged in user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_user(username, async=True)
        >>> result = thread.get()

        :param async bool
        :param str username: The name that needs to be deleted (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_user_with_http_info(username, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_user_with_http_info(username, **kwargs)  # noqa: E501
            return data

    def delete_user_with_http_info(self, username, **kwargs):  # noqa: E501
        """Delete user  # noqa: E501

        This can only be done by the logged in user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_user_with_http_info(username, async=True)
        >>> result = thread.get()

        :param async bool
        :param str username: The name that needs to be deleted (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['username']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_user" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'username' is set
        if ('username' not in local_var_params or
                local_var_params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `delete_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'username' in local_var_params:
            path_params['username'] = local_var_params['username']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/user/{username}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=local_var_params.get('async'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_by_name(self, username, **kwargs):  # noqa: E501
        """Get user by user name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_user_by_name(username, async=True)
        >>> result = thread.get()

        :param async bool
        :param str username: The name that needs to be fetched. Use user1 for testing. (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_user_by_name_with_http_info(username, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_by_name_with_http_info(username, **kwargs)  # noqa: E501
            return data

    def get_user_by_name_with_http_info(self, username, **kwargs):  # noqa: E501
        """Get user by user name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_user_by_name_with_http_info(username, async=True)
        >>> result = thread.get()

        :param async bool
        :param str username: The name that needs to be fetched. Use user1 for testing. (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['username']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_by_name" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'username' is set
        if ('username' not in local_var_params or
                local_var_params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `get_user_by_name`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'username' in local_var_params:
            path_params['username'] = local_var_params['username']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/user/{username}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='User',  # noqa: E501
            auth_settings=auth_settings,
            async=local_var_params.get('async'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def login_user(self, username, password, **kwargs):  # noqa: E501
        """Logs user into the system  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.login_user(username, password, async=True)
        >>> result = thread.get()

        :param async bool
        :param str username: The user name for login (required)
        :param str password: The password for login in clear text (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.login_user_with_http_info(username, password, **kwargs)  # noqa: E501
        else:
            (data) = self.login_user_with_http_info(username, password, **kwargs)  # noqa: E501
            return data

    def login_user_with_http_info(self, username, password, **kwargs):  # noqa: E501
        """Logs user into the system  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.login_user_with_http_info(username, password, async=True)
        >>> result = thread.get()

        :param async bool
        :param str username: The user name for login (required)
        :param str password: The password for login in clear text (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['username', 'password']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method login_user" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'username' is set
        if ('username' not in local_var_params or
                local_var_params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `login_user`")  # noqa: E501
        # verify the required parameter 'password' is set
        if ('password' not in local_var_params or
                local_var_params['password'] is None):
            raise ValueError("Missing the required parameter `password` when calling `login_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'username' in local_var_params:
            query_params.append(('username', local_var_params['username']))  # noqa: E501
        if 'password' in local_var_params:
            query_params.append(('password', local_var_params['password']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/user/login', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async=local_var_params.get('async'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def logout_user(self, **kwargs):  # noqa: E501
        """Logs out current logged in user session  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.logout_user(async=True)
        >>> result = thread.get()

        :param async bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.logout_user_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.logout_user_with_http_info(**kwargs)  # noqa: E501
            return data

    def logout_user_with_http_info(self, **kwargs):  # noqa: E501
        """Logs out current logged in user session  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.logout_user_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method logout_user" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/user/logout', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=local_var_params.get('async'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_user(self, username, user, **kwargs):  # noqa: E501
        """Updated user  # noqa: E501

        This can only be done by the logged in user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_user(username, user, async=True)
        >>> result = thread.get()

        :param async bool
        :param str username: name that need to be deleted (required)
        :param User user: Updated user object (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_user_with_http_info(username, user, **kwargs)  # noqa: E501
        else:
            (data) = self.update_user_with_http_info(username, user, **kwargs)  # noqa: E501
            return data

    def update_user_with_http_info(self, username, user, **kwargs):  # noqa: E501
        """Updated user  # noqa: E501

        This can only be done by the logged in user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_user_with_http_info(username, user, async=True)
        >>> result = thread.get()

        :param async bool
        :param str username: name that need to be deleted (required)
        :param User user: Updated user object (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['username', 'user']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_user" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'username' is set
        if ('username' not in local_var_params or
                local_var_params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `update_user`")  # noqa: E501
        # verify the required parameter 'user' is set
        if ('user' not in local_var_params or
                local_var_params['user'] is None):
            raise ValueError("Missing the required parameter `user` when calling `update_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'username' in local_var_params:
            path_params['username'] = local_var_params['username']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'user' in local_var_params:
            body_params = local_var_params['user']
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/user/{username}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=local_var_params.get('async'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
