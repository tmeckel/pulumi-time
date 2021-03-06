// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * ## Import
 *
 * This resource can be imported using the base UTC RFC3339 value and rotation years, months, days, hours, and minutes, separated by commas (`,`), e.g. for 30 days console
 *
 * ```sh
 *  $ pulumi import time:index/timeRotating:TimeRotating example 2020-02-12T06:36:13Z,0,0,30,0,0
 * ```
 *
 *  Otherwise, to import with the rotation RFC3339 value, the base UTC RFC3339 value and rotation UTC RFC3339 value, separated by commas (`,`), e.g. console
 *
 * ```sh
 *  $ pulumi import time:index/timeRotating:TimeRotating example 2020-02-12T06:36:13Z,2020-02-13T06:36:13Z
 * ```
 *
 *  The `triggers` argument cannot be imported.
 */
export class TimeRotating extends pulumi.CustomResource {
    /**
     * Get an existing TimeRotating resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TimeRotatingState, opts?: pulumi.CustomResourceOptions): TimeRotating {
        return new TimeRotating(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'time:index/timeRotating:TimeRotating';

    /**
     * Returns true if the given object is an instance of TimeRotating.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is TimeRotating {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === TimeRotating.__pulumiType;
    }

    /**
     * Number day of timestamp.
     */
    public /*out*/ readonly day!: pulumi.Output<number>;
    /**
     * Number hour of timestamp.
     */
    public /*out*/ readonly hour!: pulumi.Output<number>;
    /**
     * Number minute of timestamp.
     */
    public /*out*/ readonly minute!: pulumi.Output<number>;
    /**
     * Number month of timestamp.
     */
    public /*out*/ readonly month!: pulumi.Output<number>;
    /**
     * Configure the base timestamp with an UTC [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) (`YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
     */
    public readonly rfc3339!: pulumi.Output<string>;
    /**
     * Number of days to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. Conflicts with other `rotation_` arguments.
     */
    public readonly rotationDays!: pulumi.Output<number | undefined>;
    /**
     * Number of hours to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. Conflicts with other `rotation_` arguments.
     */
    public readonly rotationHours!: pulumi.Output<number | undefined>;
    /**
     * Number of minutes to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. Conflicts with other `rotation_` arguments.
     */
    public readonly rotationMinutes!: pulumi.Output<number | undefined>;
    /**
     * Number of months to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. Conflicts with other `rotation_` arguments.
     */
    public readonly rotationMonths!: pulumi.Output<number | undefined>;
    /**
     * Configure the rotation timestamp with an UTC [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) (`YYYY-MM-DDTHH:MM:SSZ`). When the current time has passed the rotation timestamp, the resource will trigger recreation. Conflicts with other `rotation_` arguments.
     */
    public readonly rotationRfc3339!: pulumi.Output<string>;
    /**
     * Number of years to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. Conflicts with other `rotation_` arguments.
     */
    public readonly rotationYears!: pulumi.Output<number | undefined>;
    /**
     * Number second of timestamp.
     */
    public /*out*/ readonly second!: pulumi.Output<number>;
    /**
     * Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. These conditions recreate the resource in addition to other rotation arguments. See the main provider documentation for more information.
     */
    public readonly triggers!: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * Number of seconds since epoch time, e.g. `1581489373`.
     */
    public /*out*/ readonly unix!: pulumi.Output<number>;
    /**
     * Number year of timestamp.
     */
    public /*out*/ readonly year!: pulumi.Output<number>;

    /**
     * Create a TimeRotating resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: TimeRotatingArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: TimeRotatingArgs | TimeRotatingState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as TimeRotatingState | undefined;
            inputs["day"] = state ? state.day : undefined;
            inputs["hour"] = state ? state.hour : undefined;
            inputs["minute"] = state ? state.minute : undefined;
            inputs["month"] = state ? state.month : undefined;
            inputs["rfc3339"] = state ? state.rfc3339 : undefined;
            inputs["rotationDays"] = state ? state.rotationDays : undefined;
            inputs["rotationHours"] = state ? state.rotationHours : undefined;
            inputs["rotationMinutes"] = state ? state.rotationMinutes : undefined;
            inputs["rotationMonths"] = state ? state.rotationMonths : undefined;
            inputs["rotationRfc3339"] = state ? state.rotationRfc3339 : undefined;
            inputs["rotationYears"] = state ? state.rotationYears : undefined;
            inputs["second"] = state ? state.second : undefined;
            inputs["triggers"] = state ? state.triggers : undefined;
            inputs["unix"] = state ? state.unix : undefined;
            inputs["year"] = state ? state.year : undefined;
        } else {
            const args = argsOrState as TimeRotatingArgs | undefined;
            inputs["rfc3339"] = args ? args.rfc3339 : undefined;
            inputs["rotationDays"] = args ? args.rotationDays : undefined;
            inputs["rotationHours"] = args ? args.rotationHours : undefined;
            inputs["rotationMinutes"] = args ? args.rotationMinutes : undefined;
            inputs["rotationMonths"] = args ? args.rotationMonths : undefined;
            inputs["rotationRfc3339"] = args ? args.rotationRfc3339 : undefined;
            inputs["rotationYears"] = args ? args.rotationYears : undefined;
            inputs["triggers"] = args ? args.triggers : undefined;
            inputs["day"] = undefined /*out*/;
            inputs["hour"] = undefined /*out*/;
            inputs["minute"] = undefined /*out*/;
            inputs["month"] = undefined /*out*/;
            inputs["second"] = undefined /*out*/;
            inputs["unix"] = undefined /*out*/;
            inputs["year"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(TimeRotating.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering TimeRotating resources.
 */
export interface TimeRotatingState {
    /**
     * Number day of timestamp.
     */
    day?: pulumi.Input<number>;
    /**
     * Number hour of timestamp.
     */
    hour?: pulumi.Input<number>;
    /**
     * Number minute of timestamp.
     */
    minute?: pulumi.Input<number>;
    /**
     * Number month of timestamp.
     */
    month?: pulumi.Input<number>;
    /**
     * Configure the base timestamp with an UTC [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) (`YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
     */
    rfc3339?: pulumi.Input<string>;
    /**
     * Number of days to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. Conflicts with other `rotation_` arguments.
     */
    rotationDays?: pulumi.Input<number>;
    /**
     * Number of hours to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. Conflicts with other `rotation_` arguments.
     */
    rotationHours?: pulumi.Input<number>;
    /**
     * Number of minutes to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. Conflicts with other `rotation_` arguments.
     */
    rotationMinutes?: pulumi.Input<number>;
    /**
     * Number of months to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. Conflicts with other `rotation_` arguments.
     */
    rotationMonths?: pulumi.Input<number>;
    /**
     * Configure the rotation timestamp with an UTC [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) (`YYYY-MM-DDTHH:MM:SSZ`). When the current time has passed the rotation timestamp, the resource will trigger recreation. Conflicts with other `rotation_` arguments.
     */
    rotationRfc3339?: pulumi.Input<string>;
    /**
     * Number of years to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. Conflicts with other `rotation_` arguments.
     */
    rotationYears?: pulumi.Input<number>;
    /**
     * Number second of timestamp.
     */
    second?: pulumi.Input<number>;
    /**
     * Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. These conditions recreate the resource in addition to other rotation arguments. See the main provider documentation for more information.
     */
    triggers?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * Number of seconds since epoch time, e.g. `1581489373`.
     */
    unix?: pulumi.Input<number>;
    /**
     * Number year of timestamp.
     */
    year?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a TimeRotating resource.
 */
export interface TimeRotatingArgs {
    /**
     * Configure the base timestamp with an UTC [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) (`YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
     */
    rfc3339?: pulumi.Input<string>;
    /**
     * Number of days to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. Conflicts with other `rotation_` arguments.
     */
    rotationDays?: pulumi.Input<number>;
    /**
     * Number of hours to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. Conflicts with other `rotation_` arguments.
     */
    rotationHours?: pulumi.Input<number>;
    /**
     * Number of minutes to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. Conflicts with other `rotation_` arguments.
     */
    rotationMinutes?: pulumi.Input<number>;
    /**
     * Number of months to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. Conflicts with other `rotation_` arguments.
     */
    rotationMonths?: pulumi.Input<number>;
    /**
     * Configure the rotation timestamp with an UTC [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) (`YYYY-MM-DDTHH:MM:SSZ`). When the current time has passed the rotation timestamp, the resource will trigger recreation. Conflicts with other `rotation_` arguments.
     */
    rotationRfc3339?: pulumi.Input<string>;
    /**
     * Number of years to add to the base timestamp to configure the rotation timestamp. When the current time has passed the rotation timestamp, the resource will trigger recreation. Conflicts with other `rotation_` arguments.
     */
    rotationYears?: pulumi.Input<number>;
    /**
     * Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. These conditions recreate the resource in addition to other rotation arguments. See the main provider documentation for more information.
     */
    triggers?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
}
