# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['TimeStaticArgs', 'TimeStatic']

@pulumi.input_type
class TimeStaticArgs:
    def __init__(__self__, *,
                 rfc3339: Optional[pulumi.Input[str]] = None,
                 triggers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a TimeStatic resource.
        :param pulumi.Input[str] rfc3339: Configure the base timestamp with an UTC [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) (`YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] triggers: Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. See the main provider documentation for more information.
        """
        if rfc3339 is not None:
            pulumi.set(__self__, "rfc3339", rfc3339)
        if triggers is not None:
            pulumi.set(__self__, "triggers", triggers)

    @property
    @pulumi.getter
    def rfc3339(self) -> Optional[pulumi.Input[str]]:
        """
        Configure the base timestamp with an UTC [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) (`YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
        """
        return pulumi.get(self, "rfc3339")

    @rfc3339.setter
    def rfc3339(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rfc3339", value)

    @property
    @pulumi.getter
    def triggers(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. See the main provider documentation for more information.
        """
        return pulumi.get(self, "triggers")

    @triggers.setter
    def triggers(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "triggers", value)


@pulumi.input_type
class _TimeStaticState:
    def __init__(__self__, *,
                 day: Optional[pulumi.Input[int]] = None,
                 hour: Optional[pulumi.Input[int]] = None,
                 minute: Optional[pulumi.Input[int]] = None,
                 month: Optional[pulumi.Input[int]] = None,
                 rfc3339: Optional[pulumi.Input[str]] = None,
                 second: Optional[pulumi.Input[int]] = None,
                 triggers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 unix: Optional[pulumi.Input[int]] = None,
                 year: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering TimeStatic resources.
        :param pulumi.Input[int] day: Number day of timestamp.
        :param pulumi.Input[int] hour: Number hour of timestamp.
        :param pulumi.Input[int] minute: Number minute of timestamp.
        :param pulumi.Input[int] month: Number month of timestamp.
        :param pulumi.Input[str] rfc3339: Configure the base timestamp with an UTC [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) (`YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
        :param pulumi.Input[int] second: Number second of timestamp.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] triggers: Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. See the main provider documentation for more information.
        :param pulumi.Input[int] unix: Number of seconds since epoch time, e.g. `1581489373`.
        :param pulumi.Input[int] year: Number year of timestamp.
        """
        if day is not None:
            pulumi.set(__self__, "day", day)
        if hour is not None:
            pulumi.set(__self__, "hour", hour)
        if minute is not None:
            pulumi.set(__self__, "minute", minute)
        if month is not None:
            pulumi.set(__self__, "month", month)
        if rfc3339 is not None:
            pulumi.set(__self__, "rfc3339", rfc3339)
        if second is not None:
            pulumi.set(__self__, "second", second)
        if triggers is not None:
            pulumi.set(__self__, "triggers", triggers)
        if unix is not None:
            pulumi.set(__self__, "unix", unix)
        if year is not None:
            pulumi.set(__self__, "year", year)

    @property
    @pulumi.getter
    def day(self) -> Optional[pulumi.Input[int]]:
        """
        Number day of timestamp.
        """
        return pulumi.get(self, "day")

    @day.setter
    def day(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "day", value)

    @property
    @pulumi.getter
    def hour(self) -> Optional[pulumi.Input[int]]:
        """
        Number hour of timestamp.
        """
        return pulumi.get(self, "hour")

    @hour.setter
    def hour(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "hour", value)

    @property
    @pulumi.getter
    def minute(self) -> Optional[pulumi.Input[int]]:
        """
        Number minute of timestamp.
        """
        return pulumi.get(self, "minute")

    @minute.setter
    def minute(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "minute", value)

    @property
    @pulumi.getter
    def month(self) -> Optional[pulumi.Input[int]]:
        """
        Number month of timestamp.
        """
        return pulumi.get(self, "month")

    @month.setter
    def month(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "month", value)

    @property
    @pulumi.getter
    def rfc3339(self) -> Optional[pulumi.Input[str]]:
        """
        Configure the base timestamp with an UTC [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) (`YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
        """
        return pulumi.get(self, "rfc3339")

    @rfc3339.setter
    def rfc3339(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rfc3339", value)

    @property
    @pulumi.getter
    def second(self) -> Optional[pulumi.Input[int]]:
        """
        Number second of timestamp.
        """
        return pulumi.get(self, "second")

    @second.setter
    def second(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "second", value)

    @property
    @pulumi.getter
    def triggers(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. See the main provider documentation for more information.
        """
        return pulumi.get(self, "triggers")

    @triggers.setter
    def triggers(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "triggers", value)

    @property
    @pulumi.getter
    def unix(self) -> Optional[pulumi.Input[int]]:
        """
        Number of seconds since epoch time, e.g. `1581489373`.
        """
        return pulumi.get(self, "unix")

    @unix.setter
    def unix(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "unix", value)

    @property
    @pulumi.getter
    def year(self) -> Optional[pulumi.Input[int]]:
        """
        Number year of timestamp.
        """
        return pulumi.get(self, "year")

    @year.setter
    def year(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "year", value)


class TimeStatic(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 rfc3339: Optional[pulumi.Input[str]] = None,
                 triggers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        ## Import

        This resource can be imported using the UTC RFC3339 value, e.g. console

        ```sh
         $ pulumi import time:index/timeStatic:TimeStatic example 2020-02-12T06:36:13Z
        ```

         The `triggers` argument cannot be imported.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] rfc3339: Configure the base timestamp with an UTC [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) (`YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] triggers: Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. See the main provider documentation for more information.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[TimeStaticArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Import

        This resource can be imported using the UTC RFC3339 value, e.g. console

        ```sh
         $ pulumi import time:index/timeStatic:TimeStatic example 2020-02-12T06:36:13Z
        ```

         The `triggers` argument cannot be imported.

        :param str resource_name: The name of the resource.
        :param TimeStaticArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TimeStaticArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 rfc3339: Optional[pulumi.Input[str]] = None,
                 triggers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TimeStaticArgs.__new__(TimeStaticArgs)

            __props__.__dict__["rfc3339"] = rfc3339
            __props__.__dict__["triggers"] = triggers
            __props__.__dict__["day"] = None
            __props__.__dict__["hour"] = None
            __props__.__dict__["minute"] = None
            __props__.__dict__["month"] = None
            __props__.__dict__["second"] = None
            __props__.__dict__["unix"] = None
            __props__.__dict__["year"] = None
        super(TimeStatic, __self__).__init__(
            'time:index/timeStatic:TimeStatic',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            day: Optional[pulumi.Input[int]] = None,
            hour: Optional[pulumi.Input[int]] = None,
            minute: Optional[pulumi.Input[int]] = None,
            month: Optional[pulumi.Input[int]] = None,
            rfc3339: Optional[pulumi.Input[str]] = None,
            second: Optional[pulumi.Input[int]] = None,
            triggers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            unix: Optional[pulumi.Input[int]] = None,
            year: Optional[pulumi.Input[int]] = None) -> 'TimeStatic':
        """
        Get an existing TimeStatic resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] day: Number day of timestamp.
        :param pulumi.Input[int] hour: Number hour of timestamp.
        :param pulumi.Input[int] minute: Number minute of timestamp.
        :param pulumi.Input[int] month: Number month of timestamp.
        :param pulumi.Input[str] rfc3339: Configure the base timestamp with an UTC [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) (`YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
        :param pulumi.Input[int] second: Number second of timestamp.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] triggers: Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. See the main provider documentation for more information.
        :param pulumi.Input[int] unix: Number of seconds since epoch time, e.g. `1581489373`.
        :param pulumi.Input[int] year: Number year of timestamp.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TimeStaticState.__new__(_TimeStaticState)

        __props__.__dict__["day"] = day
        __props__.__dict__["hour"] = hour
        __props__.__dict__["minute"] = minute
        __props__.__dict__["month"] = month
        __props__.__dict__["rfc3339"] = rfc3339
        __props__.__dict__["second"] = second
        __props__.__dict__["triggers"] = triggers
        __props__.__dict__["unix"] = unix
        __props__.__dict__["year"] = year
        return TimeStatic(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def day(self) -> pulumi.Output[int]:
        """
        Number day of timestamp.
        """
        return pulumi.get(self, "day")

    @property
    @pulumi.getter
    def hour(self) -> pulumi.Output[int]:
        """
        Number hour of timestamp.
        """
        return pulumi.get(self, "hour")

    @property
    @pulumi.getter
    def minute(self) -> pulumi.Output[int]:
        """
        Number minute of timestamp.
        """
        return pulumi.get(self, "minute")

    @property
    @pulumi.getter
    def month(self) -> pulumi.Output[int]:
        """
        Number month of timestamp.
        """
        return pulumi.get(self, "month")

    @property
    @pulumi.getter
    def rfc3339(self) -> pulumi.Output[str]:
        """
        Configure the base timestamp with an UTC [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) (`YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
        """
        return pulumi.get(self, "rfc3339")

    @property
    @pulumi.getter
    def second(self) -> pulumi.Output[int]:
        """
        Number second of timestamp.
        """
        return pulumi.get(self, "second")

    @property
    @pulumi.getter
    def triggers(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. See the main provider documentation for more information.
        """
        return pulumi.get(self, "triggers")

    @property
    @pulumi.getter
    def unix(self) -> pulumi.Output[int]:
        """
        Number of seconds since epoch time, e.g. `1581489373`.
        """
        return pulumi.get(self, "unix")

    @property
    @pulumi.getter
    def year(self) -> pulumi.Output[int]:
        """
        Number year of timestamp.
        """
        return pulumi.get(self, "year")
