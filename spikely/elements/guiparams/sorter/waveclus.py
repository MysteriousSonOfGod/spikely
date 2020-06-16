from spikesorters.waveclus import WaveClusSorter
class_default = WaveClusSorter._default_params

gui_params = [
    {
        "name": "output_folder",
        "type": "folder",
        "value": None,
        "default": None,
        "title": "Sorting output folder path.",
        "base_param": True,
    },
    {
        "name": "verbose",
        "type": "bool",
        "value": False,
        "default": False,
        "title": "If True, output from SpikeInterface element is verbose when run.",
        "base_param": True,
    },
    {
        "name": "grouping_property",
        "type": "str",
        "value": None,
        "default": None,
        "title": "Property name to be used for sorter output grouping.",
        "base_param": True,
    },
    {
        "name": "parallel",
        "type": "bool",
        "value": False,
        "default": False,
        "title": "If grouping property specifed, sort property groups in parallel if True.",
        "base_param": True,
    },
    {
        "name": "delete_output_folder",
        "type": "bool",
        "value": False,
        "default": False,
        "title": "Delete specified or default output folder on completion if True.",
        "base_param": True,
    },
    # waveclus specific parameters
    {
        "name": "detect_threshold",
        "type": "float",
        "value": 5.0,
        "default": 5.0,
        "title": "Relative detection threshold",
    },
    {
        "name": "detect_sign",
        "type": "int",
        "value": -1,
        "default": -1,
        "title": "Use -1, 0, or 1, depending on the sign of the spikes in the recording",
    },
    {
        "name": "feature_type",
        "type": "str",
        "value": "wav",
        "default": "wav",
        "title": "Feature type ('wav', 'pca')",
    },
    {
        "name": "scales",
        "type": "int",
        "value": 4,
        "default": 4,
        "title": "Number of wavelet scales",
    },
    {
        "name": "min_clus",
        "type": "int",
        "value": 20,
        "default": 20,
        "title": "Minimum size of a cluster",
    },
    {
        "name": "maxtemp",
        "type": "float",
        "value": 0.251,
        "default": 0.251,
        "title": "Maximum temperature for SPC",
    },
    {
        "name": "template_sdnum",
        "type": "int",
        "value": 3,
        "default": 3,
        "title": "Max radius of cluster in std devs",
    },
    {
        "name": "enable_detect_filter",
        "type": "bool",
        "value": class_default["enable_detect_filter"],
        "default": class_default["enable_detect_filter"],
        "title": "If true, enable detect filter.",
    },
    {
        "name": "enable_sort_filter",
        "type": "bool",
        "value": class_default["enable_sort_filter"],
        "default": class_default["enable_sort_filter"],
        "title": "If true, enable sort filter.",
    },
    {
        "name": "detect_filter_fmin",
        "type": "float",
        "value": class_default["detect_filter_fmin"],
        "default": class_default["detect_filter_fmin"],
        "title": "Minimum detection filter frequency.",
    },
    {
        "name": "detect_filter_fmax",
        "type": "float",
        "value": class_default["detect_filter_fmax"],
        "default": class_default["detect_filter_fmax"],
        "title": "Maximum detection filter frequency.",
    },
    {
        "name": "detect_filter_order",
        "type": "int",
        "value": class_default["detect_filter_order"],
        "default": class_default["detect_filter_order"],
        "title": "Order of the filter.",
    },
    {
        "name": "sort_filter_fmin",
        "type": "float",
        "value": class_default["sort_filter_fmin"],
        "default": class_default["sort_filter_fmin"],
        "title": "Sort filter frequency minimum.",
    },
    {
        "name": "sort_filter_fmax",
        "type": "float",
        "value": class_default["sort_filter_fmax"],
        "default": class_default["sort_filter_fmax"],
        "title": "Sort filter frequency maximum.",
    },
    {
        "name": "sort_filter_order",
        "type": "int",
        "value": class_default["sort_filter_order"],
        "default": class_default["sort_filter_order"],
        "title": "Order of the filter.",
    },
]
