// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Time
{
    /// <summary>
    /// ## Import
    /// 
    /// This resource can be imported using the UTC RFC3339 value, e.g. console
    /// 
    /// ```sh
    ///  $ pulumi import time:index/timeStatic:TimeStatic example 2020-02-12T06:36:13Z
    /// ```
    /// 
    ///  The `triggers` argument cannot be imported.
    /// </summary>
    [TimeResourceType("time:index/timeStatic:TimeStatic")]
    public partial class TimeStatic : Pulumi.CustomResource
    {
        /// <summary>
        /// Number day of timestamp.
        /// </summary>
        [Output("day")]
        public Output<int> Day { get; private set; } = null!;

        /// <summary>
        /// Number hour of timestamp.
        /// </summary>
        [Output("hour")]
        public Output<int> Hour { get; private set; } = null!;

        /// <summary>
        /// Number minute of timestamp.
        /// </summary>
        [Output("minute")]
        public Output<int> Minute { get; private set; } = null!;

        /// <summary>
        /// Number month of timestamp.
        /// </summary>
        [Output("month")]
        public Output<int> Month { get; private set; } = null!;

        /// <summary>
        /// Configure the base timestamp with an UTC [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) (`YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
        /// </summary>
        [Output("rfc3339")]
        public Output<string> Rfc3339 { get; private set; } = null!;

        /// <summary>
        /// Number second of timestamp.
        /// </summary>
        [Output("second")]
        public Output<int> Second { get; private set; } = null!;

        /// <summary>
        /// Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. See the main provider documentation for more information.
        /// </summary>
        [Output("triggers")]
        public Output<ImmutableDictionary<string, string>?> Triggers { get; private set; } = null!;

        /// <summary>
        /// Number of seconds since epoch time, e.g. `1581489373`.
        /// </summary>
        [Output("unix")]
        public Output<int> Unix { get; private set; } = null!;

        /// <summary>
        /// Number year of timestamp.
        /// </summary>
        [Output("year")]
        public Output<int> Year { get; private set; } = null!;


        /// <summary>
        /// Create a TimeStatic resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public TimeStatic(string name, TimeStaticArgs? args = null, CustomResourceOptions? options = null)
            : base("time:index/timeStatic:TimeStatic", name, args ?? new TimeStaticArgs(), MakeResourceOptions(options, ""))
        {
        }

        private TimeStatic(string name, Input<string> id, TimeStaticState? state = null, CustomResourceOptions? options = null)
            : base("time:index/timeStatic:TimeStatic", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing TimeStatic resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static TimeStatic Get(string name, Input<string> id, TimeStaticState? state = null, CustomResourceOptions? options = null)
        {
            return new TimeStatic(name, id, state, options);
        }
    }

    public sealed class TimeStaticArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Configure the base timestamp with an UTC [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) (`YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
        /// </summary>
        [Input("rfc3339")]
        public Input<string>? Rfc3339 { get; set; }

        [Input("triggers")]
        private InputMap<string>? _triggers;

        /// <summary>
        /// Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. See the main provider documentation for more information.
        /// </summary>
        public InputMap<string> Triggers
        {
            get => _triggers ?? (_triggers = new InputMap<string>());
            set => _triggers = value;
        }

        public TimeStaticArgs()
        {
        }
    }

    public sealed class TimeStaticState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Number day of timestamp.
        /// </summary>
        [Input("day")]
        public Input<int>? Day { get; set; }

        /// <summary>
        /// Number hour of timestamp.
        /// </summary>
        [Input("hour")]
        public Input<int>? Hour { get; set; }

        /// <summary>
        /// Number minute of timestamp.
        /// </summary>
        [Input("minute")]
        public Input<int>? Minute { get; set; }

        /// <summary>
        /// Number month of timestamp.
        /// </summary>
        [Input("month")]
        public Input<int>? Month { get; set; }

        /// <summary>
        /// Configure the base timestamp with an UTC [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) (`YYYY-MM-DDTHH:MM:SSZ`). Defaults to the current time.
        /// </summary>
        [Input("rfc3339")]
        public Input<string>? Rfc3339 { get; set; }

        /// <summary>
        /// Number second of timestamp.
        /// </summary>
        [Input("second")]
        public Input<int>? Second { get; set; }

        [Input("triggers")]
        private InputMap<string>? _triggers;

        /// <summary>
        /// Arbitrary map of values that, when changed, will trigger a new base timestamp value to be saved. See the main provider documentation for more information.
        /// </summary>
        public InputMap<string> Triggers
        {
            get => _triggers ?? (_triggers = new InputMap<string>());
            set => _triggers = value;
        }

        /// <summary>
        /// Number of seconds since epoch time, e.g. `1581489373`.
        /// </summary>
        [Input("unix")]
        public Input<int>? Unix { get; set; }

        /// <summary>
        /// Number year of timestamp.
        /// </summary>
        [Input("year")]
        public Input<int>? Year { get; set; }

        public TimeStaticState()
        {
        }
    }
}
