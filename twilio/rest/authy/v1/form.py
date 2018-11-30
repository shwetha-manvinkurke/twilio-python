# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class FormList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version):
        """
        Initialize the FormList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.authy.v1.form.FormList
        :rtype: twilio.rest.authy.v1.form.FormList
        """
        super(FormList, self).__init__(version)

        # Path Solution
        self._solution = {}

    def get(self, type):
        """
        Constructs a FormContext

        :param type: The Type of this Form

        :returns: twilio.rest.authy.v1.form.FormContext
        :rtype: twilio.rest.authy.v1.form.FormContext
        """
        return FormContext(self._version, type=type, )

    def __call__(self, type):
        """
        Constructs a FormContext

        :param type: The Type of this Form

        :returns: twilio.rest.authy.v1.form.FormContext
        :rtype: twilio.rest.authy.v1.form.FormContext
        """
        return FormContext(self._version, type=type, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Authy.V1.FormList>'


class FormPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the FormPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.authy.v1.form.FormPage
        :rtype: twilio.rest.authy.v1.form.FormPage
        """
        super(FormPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of FormInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.authy.v1.form.FormInstance
        :rtype: twilio.rest.authy.v1.form.FormInstance
        """
        return FormInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Authy.V1.FormPage>'


class FormContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, type):
        """
        Initialize the FormContext

        :param Version version: Version that contains the resource
        :param type: The Type of this Form

        :returns: twilio.rest.authy.v1.form.FormContext
        :rtype: twilio.rest.authy.v1.form.FormContext
        """
        super(FormContext, self).__init__(version)

        # Path Solution
        self._solution = {'type': type, }
        self._uri = '/Forms/{type}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a FormInstance

        :returns: Fetched FormInstance
        :rtype: twilio.rest.authy.v1.form.FormInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return FormInstance(self._version, payload, type=self._solution['type'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Authy.V1.FormContext {}>'.format(context)


class FormInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    class FormTypes(object):
        FORM_APP_PUSH = "form-app-push"
        FORM_SMS = "form-sms"
        FORM_TOTP = "form-totp"

    def __init__(self, version, payload, type=None):
        """
        Initialize the FormInstance

        :returns: twilio.rest.authy.v1.form.FormInstance
        :rtype: twilio.rest.authy.v1.form.FormInstance
        """
        super(FormInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'type': payload['type'],
            'forms': payload['forms'],
            'form_meta': payload['form_meta'],
            'url': payload['url'],
        }

        # Context
        self._context = None
        self._solution = {'type': type or self._properties['type'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: FormContext for this FormInstance
        :rtype: twilio.rest.authy.v1.form.FormContext
        """
        if self._context is None:
            self._context = FormContext(self._version, type=self._solution['type'], )
        return self._context

    @property
    def type(self):
        """
        :returns: The Type of this Form
        :rtype: FormInstance.FormTypes
        """
        return self._properties['type']

    @property
    def forms(self):
        """
        :returns: Object that contains the available forms for this type.
        :rtype: dict
        """
        return self._properties['forms']

    @property
    def form_meta(self):
        """
        :returns: Additional information for the available forms for this type.
        :rtype: dict
        """
        return self._properties['form_meta']

    @property
    def url(self):
        """
        :returns: The URL to access the forms for this type.
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a FormInstance

        :returns: Fetched FormInstance
        :rtype: twilio.rest.authy.v1.form.FormInstance
        """
        return self._proxy.fetch()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Authy.V1.FormInstance {}>'.format(context)
