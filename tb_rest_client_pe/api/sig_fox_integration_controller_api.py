# coding: utf-8

"""
    ThingsBoard REST API

    For instructions how to authorize requests please visit <a href='http://thingsboard.io/docs/reference/rest-api/'>REST API documentation page</a>.  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from tb_rest_client_pe.api_client import ApiClient


class SigFoxIntegrationControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def process_request_using_delete1(self, routing_key, msg, request_headers, **kwargs):  # noqa: E501
        """processRequest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.process_request_using_delete1(routing_key, msg, request_headers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str routing_key: routingKey (required)
        :param str msg: msg (required)
        :param object request_headers: requestHeaders (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.process_request_using_delete1_with_http_info(routing_key, msg, request_headers, **kwargs)  # noqa: E501
        else:
            (data) = self.process_request_using_delete1_with_http_info(routing_key, msg, request_headers, **kwargs)  # noqa: E501
            return data

    def process_request_using_delete1_with_http_info(self, routing_key, msg, request_headers, **kwargs):  # noqa: E501
        """processRequest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.process_request_using_delete1_with_http_info(routing_key, msg, request_headers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str routing_key: routingKey (required)
        :param str msg: msg (required)
        :param object request_headers: requestHeaders (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['routing_key', 'msg', 'request_headers']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method process_request_using_delete1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'routing_key' is set
        if ('routing_key' not in params or
                params['routing_key'] is None):
            raise ValueError("Missing the required parameter `routing_key` when calling `process_request_using_delete1`")  # noqa: E501
        # verify the required parameter 'msg' is set
        if ('msg' not in params or
                params['msg'] is None):
            raise ValueError("Missing the required parameter `msg` when calling `process_request_using_delete1`")  # noqa: E501
        # verify the required parameter 'request_headers' is set
        if ('request_headers' not in params or
                params['request_headers'] is None):
            raise ValueError("Missing the required parameter `request_headers` when calling `process_request_using_delete1`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'routing_key' in params:
            path_params['routingKey'] = params['routing_key']  # noqa: E501

        query_params = []

        header_params = {}
        if 'request_headers' in params:
            header_params['requestHeaders'] = params['request_headers']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'msg' in params:
            body_params = params['msg']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/integrations/sigfox/{routingKey}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeferredResultResponseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def process_request_using_get1(self, routing_key, msg, request_headers, **kwargs):  # noqa: E501
        """processRequest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.process_request_using_get1(routing_key, msg, request_headers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str routing_key: routingKey (required)
        :param str msg: msg (required)
        :param object request_headers: requestHeaders (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.process_request_using_get1_with_http_info(routing_key, msg, request_headers, **kwargs)  # noqa: E501
        else:
            (data) = self.process_request_using_get1_with_http_info(routing_key, msg, request_headers, **kwargs)  # noqa: E501
            return data

    def process_request_using_get1_with_http_info(self, routing_key, msg, request_headers, **kwargs):  # noqa: E501
        """processRequest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.process_request_using_get1_with_http_info(routing_key, msg, request_headers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str routing_key: routingKey (required)
        :param str msg: msg (required)
        :param object request_headers: requestHeaders (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['routing_key', 'msg', 'request_headers']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method process_request_using_get1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'routing_key' is set
        if ('routing_key' not in params or
                params['routing_key'] is None):
            raise ValueError("Missing the required parameter `routing_key` when calling `process_request_using_get1`")  # noqa: E501
        # verify the required parameter 'msg' is set
        if ('msg' not in params or
                params['msg'] is None):
            raise ValueError("Missing the required parameter `msg` when calling `process_request_using_get1`")  # noqa: E501
        # verify the required parameter 'request_headers' is set
        if ('request_headers' not in params or
                params['request_headers'] is None):
            raise ValueError("Missing the required parameter `request_headers` when calling `process_request_using_get1`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'routing_key' in params:
            path_params['routingKey'] = params['routing_key']  # noqa: E501

        query_params = []

        header_params = {}
        if 'request_headers' in params:
            header_params['requestHeaders'] = params['request_headers']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'msg' in params:
            body_params = params['msg']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/integrations/sigfox/{routingKey}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeferredResultResponseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def process_request_using_head1(self, routing_key, msg, request_headers, **kwargs):  # noqa: E501
        """processRequest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.process_request_using_head1(routing_key, msg, request_headers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str routing_key: routingKey (required)
        :param str msg: msg (required)
        :param object request_headers: requestHeaders (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.process_request_using_head1_with_http_info(routing_key, msg, request_headers, **kwargs)  # noqa: E501
        else:
            (data) = self.process_request_using_head1_with_http_info(routing_key, msg, request_headers, **kwargs)  # noqa: E501
            return data

    def process_request_using_head1_with_http_info(self, routing_key, msg, request_headers, **kwargs):  # noqa: E501
        """processRequest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.process_request_using_head1_with_http_info(routing_key, msg, request_headers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str routing_key: routingKey (required)
        :param str msg: msg (required)
        :param object request_headers: requestHeaders (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['routing_key', 'msg', 'request_headers']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method process_request_using_head1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'routing_key' is set
        if ('routing_key' not in params or
                params['routing_key'] is None):
            raise ValueError("Missing the required parameter `routing_key` when calling `process_request_using_head1`")  # noqa: E501
        # verify the required parameter 'msg' is set
        if ('msg' not in params or
                params['msg'] is None):
            raise ValueError("Missing the required parameter `msg` when calling `process_request_using_head1`")  # noqa: E501
        # verify the required parameter 'request_headers' is set
        if ('request_headers' not in params or
                params['request_headers'] is None):
            raise ValueError("Missing the required parameter `request_headers` when calling `process_request_using_head1`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'routing_key' in params:
            path_params['routingKey'] = params['routing_key']  # noqa: E501

        query_params = []

        header_params = {}
        if 'request_headers' in params:
            header_params['requestHeaders'] = params['request_headers']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'msg' in params:
            body_params = params['msg']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/integrations/sigfox/{routingKey}', 'HEAD',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeferredResultResponseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def process_request_using_options1(self, routing_key, msg, request_headers, **kwargs):  # noqa: E501
        """processRequest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.process_request_using_options1(routing_key, msg, request_headers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str routing_key: routingKey (required)
        :param str msg: msg (required)
        :param object request_headers: requestHeaders (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.process_request_using_options1_with_http_info(routing_key, msg, request_headers, **kwargs)  # noqa: E501
        else:
            (data) = self.process_request_using_options1_with_http_info(routing_key, msg, request_headers, **kwargs)  # noqa: E501
            return data

    def process_request_using_options1_with_http_info(self, routing_key, msg, request_headers, **kwargs):  # noqa: E501
        """processRequest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.process_request_using_options1_with_http_info(routing_key, msg, request_headers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str routing_key: routingKey (required)
        :param str msg: msg (required)
        :param object request_headers: requestHeaders (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['routing_key', 'msg', 'request_headers']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method process_request_using_options1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'routing_key' is set
        if ('routing_key' not in params or
                params['routing_key'] is None):
            raise ValueError("Missing the required parameter `routing_key` when calling `process_request_using_options1`")  # noqa: E501
        # verify the required parameter 'msg' is set
        if ('msg' not in params or
                params['msg'] is None):
            raise ValueError("Missing the required parameter `msg` when calling `process_request_using_options1`")  # noqa: E501
        # verify the required parameter 'request_headers' is set
        if ('request_headers' not in params or
                params['request_headers'] is None):
            raise ValueError("Missing the required parameter `request_headers` when calling `process_request_using_options1`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'routing_key' in params:
            path_params['routingKey'] = params['routing_key']  # noqa: E501

        query_params = []

        header_params = {}
        if 'request_headers' in params:
            header_params['requestHeaders'] = params['request_headers']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'msg' in params:
            body_params = params['msg']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/integrations/sigfox/{routingKey}', 'OPTIONS',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeferredResultResponseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def process_request_using_patch1(self, routing_key, msg, request_headers, **kwargs):  # noqa: E501
        """processRequest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.process_request_using_patch1(routing_key, msg, request_headers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str routing_key: routingKey (required)
        :param str msg: msg (required)
        :param object request_headers: requestHeaders (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.process_request_using_patch1_with_http_info(routing_key, msg, request_headers, **kwargs)  # noqa: E501
        else:
            (data) = self.process_request_using_patch1_with_http_info(routing_key, msg, request_headers, **kwargs)  # noqa: E501
            return data

    def process_request_using_patch1_with_http_info(self, routing_key, msg, request_headers, **kwargs):  # noqa: E501
        """processRequest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.process_request_using_patch1_with_http_info(routing_key, msg, request_headers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str routing_key: routingKey (required)
        :param str msg: msg (required)
        :param object request_headers: requestHeaders (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['routing_key', 'msg', 'request_headers']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method process_request_using_patch1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'routing_key' is set
        if ('routing_key' not in params or
                params['routing_key'] is None):
            raise ValueError("Missing the required parameter `routing_key` when calling `process_request_using_patch1`")  # noqa: E501
        # verify the required parameter 'msg' is set
        if ('msg' not in params or
                params['msg'] is None):
            raise ValueError("Missing the required parameter `msg` when calling `process_request_using_patch1`")  # noqa: E501
        # verify the required parameter 'request_headers' is set
        if ('request_headers' not in params or
                params['request_headers'] is None):
            raise ValueError("Missing the required parameter `request_headers` when calling `process_request_using_patch1`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'routing_key' in params:
            path_params['routingKey'] = params['routing_key']  # noqa: E501

        query_params = []

        header_params = {}
        if 'request_headers' in params:
            header_params['requestHeaders'] = params['request_headers']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'msg' in params:
            body_params = params['msg']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/integrations/sigfox/{routingKey}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeferredResultResponseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def process_request_using_post5(self, routing_key, msg, request_headers, **kwargs):  # noqa: E501
        """processRequest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.process_request_using_post5(routing_key, msg, request_headers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str routing_key: routingKey (required)
        :param str msg: msg (required)
        :param object request_headers: requestHeaders (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.process_request_using_post5_with_http_info(routing_key, msg, request_headers, **kwargs)  # noqa: E501
        else:
            (data) = self.process_request_using_post5_with_http_info(routing_key, msg, request_headers, **kwargs)  # noqa: E501
            return data

    def process_request_using_post5_with_http_info(self, routing_key, msg, request_headers, **kwargs):  # noqa: E501
        """processRequest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.process_request_using_post5_with_http_info(routing_key, msg, request_headers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str routing_key: routingKey (required)
        :param str msg: msg (required)
        :param object request_headers: requestHeaders (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['routing_key', 'msg', 'request_headers']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method process_request_using_post5" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'routing_key' is set
        if ('routing_key' not in params or
                params['routing_key'] is None):
            raise ValueError("Missing the required parameter `routing_key` when calling `process_request_using_post5`")  # noqa: E501
        # verify the required parameter 'msg' is set
        if ('msg' not in params or
                params['msg'] is None):
            raise ValueError("Missing the required parameter `msg` when calling `process_request_using_post5`")  # noqa: E501
        # verify the required parameter 'request_headers' is set
        if ('request_headers' not in params or
                params['request_headers'] is None):
            raise ValueError("Missing the required parameter `request_headers` when calling `process_request_using_post5`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'routing_key' in params:
            path_params['routingKey'] = params['routing_key']  # noqa: E501

        query_params = []

        header_params = {}
        if 'request_headers' in params:
            header_params['requestHeaders'] = params['request_headers']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'msg' in params:
            body_params = params['msg']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/integrations/sigfox/{routingKey}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeferredResultResponseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def process_request_using_put1(self, routing_key, msg, request_headers, **kwargs):  # noqa: E501
        """processRequest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.process_request_using_put1(routing_key, msg, request_headers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str routing_key: routingKey (required)
        :param str msg: msg (required)
        :param object request_headers: requestHeaders (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.process_request_using_put1_with_http_info(routing_key, msg, request_headers, **kwargs)  # noqa: E501
        else:
            (data) = self.process_request_using_put1_with_http_info(routing_key, msg, request_headers, **kwargs)  # noqa: E501
            return data

    def process_request_using_put1_with_http_info(self, routing_key, msg, request_headers, **kwargs):  # noqa: E501
        """processRequest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.process_request_using_put1_with_http_info(routing_key, msg, request_headers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str routing_key: routingKey (required)
        :param str msg: msg (required)
        :param object request_headers: requestHeaders (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['routing_key', 'msg', 'request_headers']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method process_request_using_put1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'routing_key' is set
        if ('routing_key' not in params or
                params['routing_key'] is None):
            raise ValueError("Missing the required parameter `routing_key` when calling `process_request_using_put1`")  # noqa: E501
        # verify the required parameter 'msg' is set
        if ('msg' not in params or
                params['msg'] is None):
            raise ValueError("Missing the required parameter `msg` when calling `process_request_using_put1`")  # noqa: E501
        # verify the required parameter 'request_headers' is set
        if ('request_headers' not in params or
                params['request_headers'] is None):
            raise ValueError("Missing the required parameter `request_headers` when calling `process_request_using_put1`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'routing_key' in params:
            path_params['routingKey'] = params['routing_key']  # noqa: E501

        query_params = []

        header_params = {}
        if 'request_headers' in params:
            header_params['requestHeaders'] = params['request_headers']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'msg' in params:
            body_params = params['msg']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/integrations/sigfox/{routingKey}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeferredResultResponseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)