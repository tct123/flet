import json
from typing import Any, List, Optional, Union

from flet.core.animation import AnimationValue
from flet.core.badge import BadgeValue
from flet.core.border import Border, BorderSide
from flet.core.charts.chart_axis import ChartAxis
from flet.core.charts.chart_grid_lines import ChartGridLines
from flet.core.charts.line_chart_data import LineChartData
from flet.core.constrained_control import ConstrainedControl
from flet.core.control import OptionalNumber
from flet.core.control_event import ControlEvent
from flet.core.event_handler import EventHandler
from flet.core.ref import Ref
from flet.core.tooltip import TooltipValue
from flet.core.types import (
    ColorEnums,
    ColorValue,
    OffsetValue,
    OptionalControlEventCallable,
    OptionalEventCallable,
    PaddingValue,
    ResponsiveNumber,
    RotateValue,
    ScaleValue,
)


class LineChart(ConstrainedControl):
    def __init__(
        self,
        data_series: Optional[List[LineChartData]] = None,
        animate: Optional[AnimationValue] = None,
        interactive: Optional[bool] = None,
        point_line_start: OptionalNumber = None,
        point_line_end: OptionalNumber = None,
        bgcolor: Optional[ColorValue] = None,
        tooltip_bgcolor: Optional[ColorValue] = None,
        border: Optional[Border] = None,
        horizontal_grid_lines: Optional[ChartGridLines] = None,
        vertical_grid_lines: Optional[ChartGridLines] = None,
        left_axis: Optional[ChartAxis] = None,
        top_axis: Optional[ChartAxis] = None,
        right_axis: Optional[ChartAxis] = None,
        bottom_axis: Optional[ChartAxis] = None,
        baseline_x: OptionalNumber = None,
        min_x: OptionalNumber = None,
        max_x: OptionalNumber = None,
        baseline_y: OptionalNumber = None,
        min_y: OptionalNumber = None,
        max_y: OptionalNumber = None,
        tooltip_rounded_radius: OptionalNumber = None,
        tooltip_margin: OptionalNumber = None,
        tooltip_padding: Optional[PaddingValue] = None,
        tooltip_max_content_width: OptionalNumber = None,
        tooltip_rotate_angle: OptionalNumber = None,
        tooltip_tooltip_horizontal_offset: OptionalNumber = None,
        tooltip_tooltip_border_side: Optional[BorderSide] = None,
        tooltip_fit_inside_horizontally: Optional[bool] = None,
        tooltip_fit_inside_vertically: Optional[bool] = None,
        tooltip_show_on_top_of_chart_box_area: Optional[bool] = None,
        on_chart_event: OptionalEventCallable["LineChartEvent"] = None,
        #
        # ConstrainedControl
        #
        ref: Optional[Ref] = None,
        width: OptionalNumber = None,
        height: OptionalNumber = None,
        left: OptionalNumber = None,
        top: OptionalNumber = None,
        right: OptionalNumber = None,
        bottom: OptionalNumber = None,
        expand: Union[None, bool, int] = None,
        expand_loose: Optional[bool] = None,
        col: Optional[ResponsiveNumber] = None,
        opacity: OptionalNumber = None,
        rotate: Optional[RotateValue] = None,
        scale: Optional[ScaleValue] = None,
        offset: Optional[OffsetValue] = None,
        aspect_ratio: OptionalNumber = None,
        animate_opacity: Optional[AnimationValue] = None,
        animate_size: Optional[AnimationValue] = None,
        animate_position: Optional[AnimationValue] = None,
        animate_rotation: Optional[AnimationValue] = None,
        animate_scale: Optional[AnimationValue] = None,
        animate_offset: Optional[AnimationValue] = None,
        on_animation_end: OptionalControlEventCallable = None,
        tooltip: Optional[TooltipValue] = None,
        badge: Optional[BadgeValue] = None,
        visible: Optional[bool] = None,
        disabled: Optional[bool] = None,
        data: Any = None,
    ):
        ConstrainedControl.__init__(
            self,
            ref=ref,
            width=width,
            height=height,
            left=left,
            top=top,
            right=right,
            bottom=bottom,
            expand=expand,
            expand_loose=expand_loose,
            col=col,
            opacity=opacity,
            rotate=rotate,
            scale=scale,
            offset=offset,
            aspect_ratio=aspect_ratio,
            animate_opacity=animate_opacity,
            animate_size=animate_size,
            animate_position=animate_position,
            animate_rotation=animate_rotation,
            animate_scale=animate_scale,
            animate_offset=animate_offset,
            on_animation_end=on_animation_end,
            tooltip=tooltip,
            badge=badge,
            visible=visible,
            disabled=disabled,
            data=data,
        )

        self.__on_chart_event = EventHandler(lambda e: LineChartEvent(e))
        self._add_event_handler("chart_event", self.__on_chart_event.get_handler())

        self.data_series = data_series
        self.animate = animate
        self.interactive = interactive
        self.point_line_start = point_line_start
        self.point_line_end = point_line_end
        self.bgcolor = bgcolor
        self.tooltip_bgcolor = tooltip_bgcolor
        self.border = border
        self.horizontal_grid_lines = horizontal_grid_lines
        self.vertical_grid_lines = vertical_grid_lines
        self.left_axis = left_axis
        self.top_axis = top_axis
        self.right_axis = right_axis
        self.bottom_axis = bottom_axis
        self.baseline_x = baseline_x
        self.baseline_y = baseline_y
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.on_chart_event = on_chart_event
        self.tooltip_rounded_radius = tooltip_rounded_radius
        self.tooltip_margin = tooltip_margin
        self.tooltip_padding = tooltip_padding
        self.tooltip_max_content_width = tooltip_max_content_width
        self.tooltip_rotate_angle = tooltip_rotate_angle
        self.tooltip_horizontal_offset = tooltip_tooltip_horizontal_offset
        self.tooltip_border_side = tooltip_tooltip_border_side
        self.tooltip_fit_inside_horizontally = tooltip_fit_inside_horizontally
        self.tooltip_fit_inside_vertically = tooltip_fit_inside_vertically
        self.tooltip_show_on_top_of_chart_box_area = (
            tooltip_show_on_top_of_chart_box_area
        )

    def _get_control_name(self):
        return "linechart"

    def before_update(self):
        super().before_update()
        self._set_attr_json("horizontalGridLines", self.__horizontal_grid_lines)
        self._set_attr_json("verticalGridLines", self.__vertical_grid_lines)
        self._set_attr_json("animate", self.__animate)
        self._set_attr_json("border", self.__border)
        self._set_attr_json("tooltipBorderSide", self.__tooltip_border_side)
        self._set_attr_json("tooltipPadding", self.__tooltip_padding)

    def _get_children(self):
        children = []
        for ds in self.__data_series:
            children.append(ds)
        if self.__left_axis:
            self.__left_axis._set_attr_internal("n", "l")
            children.append(self.__left_axis)
        if self.__top_axis:
            self.__top_axis._set_attr_internal("n", "t")
            children.append(self.__top_axis)
        if self.__right_axis:
            self.__right_axis._set_attr_internal("n", "r")
            children.append(self.__right_axis)
        if self.__bottom_axis:
            self.__bottom_axis._set_attr_internal("n", "b")
            children.append(self.__bottom_axis)
        return children

    # data_series
    @property
    def data_series(self):
        return self.__data_series

    @data_series.setter
    def data_series(self, value):
        self.__data_series = value if value is not None else []

    # animate
    @property
    def animate(self) -> AnimationValue:
        return self.__animate

    @animate.setter
    def animate(self, value: AnimationValue):
        self.__animate = value

    # bgcolor
    @property
    def bgcolor(self) -> Optional[ColorValue]:
        return self.__bgcolor

    @bgcolor.setter
    def bgcolor(self, value: Optional[ColorValue]):
        self.__bgcolor = value
        self._set_enum_attr("bgcolor", value, ColorEnums)

    # interactive
    @property
    def interactive(self) -> bool:
        return self._get_attr("interactive", data_type="bool", def_value=True)

    @interactive.setter
    def interactive(self, value: Optional[bool]):
        self._set_attr("interactive", value)

    # point_line_start
    @property
    def point_line_start(self) -> OptionalNumber:
        return self._get_attr("pointLineStart", data_type="float")

    @point_line_start.setter
    def point_line_start(self, value: OptionalNumber):
        self._set_attr("pointLineStart", value)

    # point_line_end
    @property
    def point_line_end(self) -> OptionalNumber:
        return self._get_attr("pointLineEnd", data_type="float")

    @point_line_end.setter
    def point_line_end(self, value: OptionalNumber):
        self._set_attr("pointLineEnd", value)

    # tooltip_bgcolor
    @property
    def tooltip_bgcolor(self) -> Optional[str]:
        return self.__tooltip_bgcolor

    @tooltip_bgcolor.setter
    def tooltip_bgcolor(self, value: Optional[str]):
        self.__tooltip_bgcolor = value
        self._set_enum_attr("tooltipBgcolor", value, ColorEnums)

    # border
    @property
    def border(self) -> Optional[Border]:
        return self.__border

    @border.setter
    def border(self, value: Optional[Border]):
        self.__border = value

    # horizontal_grid_lines
    @property
    def horizontal_grid_lines(self) -> Optional[ChartGridLines]:
        return self.__horizontal_grid_lines

    @horizontal_grid_lines.setter
    def horizontal_grid_lines(self, value: Optional[ChartGridLines]):
        self.__horizontal_grid_lines = value

    # vertical_grid_lines
    @property
    def vertical_grid_lines(self) -> Optional[ChartGridLines]:
        return self.__vertical_grid_lines

    @vertical_grid_lines.setter
    def vertical_grid_lines(self, value: Optional[ChartGridLines]):
        self.__vertical_grid_lines = value

    # left_axis
    @property
    def left_axis(self) -> Optional[ChartAxis]:
        return self.__left_axis

    @left_axis.setter
    def left_axis(self, value: Optional[ChartAxis]):
        self.__left_axis = value

    # top_axis
    @property
    def top_axis(self) -> Optional[ChartAxis]:
        return self.__top_axis

    @top_axis.setter
    def top_axis(self, value: Optional[ChartAxis]):
        self.__top_axis = value

    # right_axis
    @property
    def right_axis(self) -> Optional[ChartAxis]:
        return self.__right_axis

    @right_axis.setter
    def right_axis(self, value: Optional[ChartAxis]):
        self.__right_axis = value

    # bottom_axis
    @property
    def bottom_axis(self) -> Optional[ChartAxis]:
        return self.__bottom_axis

    @bottom_axis.setter
    def bottom_axis(self, value: Optional[ChartAxis]):
        self.__bottom_axis = value

    # baseline_x
    @property
    def baseline_x(self) -> OptionalNumber:
        return self._get_attr("baselinex", data_type="float")

    @baseline_x.setter
    def baseline_x(self, value: OptionalNumber):
        self._set_attr("baselineX", value)

    # baseline_y
    @property
    def baseline_y(self) -> OptionalNumber:
        return self._get_attr("baselineY", data_type="float")

    @baseline_y.setter
    def baseline_y(self, value: OptionalNumber):
        self._set_attr("baselineY", value)

    # min_x
    @property
    def min_x(self) -> OptionalNumber:
        return self._get_attr("minX", data_type="float")

    @min_x.setter
    def min_x(self, value: OptionalNumber):
        self._set_attr("minX", value)

    # max_x
    @property
    def max_x(self) -> OptionalNumber:
        return self._get_attr("maxX", data_type="float")

    @max_x.setter
    def max_x(self, value: OptionalNumber):
        self._set_attr("maxX", value)

    # min_y
    @property
    def min_y(self) -> OptionalNumber:
        return self._get_attr("minY", data_type="float")

    @min_y.setter
    def min_y(self, value: OptionalNumber):
        self._set_attr("minY", value)

    # max_y
    @property
    def max_y(self) -> OptionalNumber:
        return self._get_attr("maxY", data_type="float")

    @max_y.setter
    def max_y(self, value: OptionalNumber):
        self._set_attr("maxY", value)

    # tooltip_rounded_radius
    @property
    def tooltip_rounded_radius(self) -> OptionalNumber:
        return self._get_attr("tooltipRoundedRadius", data_type="float", def_value=4)

    @tooltip_rounded_radius.setter
    def tooltip_rounded_radius(self, value: OptionalNumber):
        self._set_attr("tooltipRoundedRadius", value)

    # tooltip_margin
    @property
    def tooltip_margin(self) -> OptionalNumber:
        return self._get_attr("tooltipMargin", data_type="float", def_value=16)

    @tooltip_margin.setter
    def tooltip_margin(self, value: OptionalNumber):
        self._set_attr("tooltipMargin", value)

    # tooltip_padding
    @property
    def tooltip_padding(self) -> Optional[PaddingValue]:
        return self.__tooltip_padding

    @tooltip_padding.setter
    def tooltip_padding(self, value: Optional[PaddingValue]):
        self.__tooltip_padding = value

    # tooltip_max_content_width
    @property
    def tooltip_max_content_width(self) -> OptionalNumber:
        return self._get_attr(
            "tooltipMaxContentWidth", data_type="float", def_value=120
        )

    @tooltip_max_content_width.setter
    def tooltip_max_content_width(self, value: OptionalNumber):
        self._set_attr("tooltipMaxContentWidth", value)

    # tooltip_rotate_angle
    @property
    def tooltip_rotate_angle(self) -> OptionalNumber:
        return self._get_attr("tooltipRotateAngle", data_type="float", def_value=0.0)

    @tooltip_rotate_angle.setter
    def tooltip_rotate_angle(self, value: OptionalNumber):
        self._set_attr("tooltipRotateAngle", value)

    # tooltip_fit_inside_vertically
    @property
    def tooltip_fit_inside_vertically(self) -> Optional[bool]:
        return self._get_attr(
            "tooltipFitInsideVertically", data_type="bool", def_value=False
        )

    @tooltip_fit_inside_vertically.setter
    def tooltip_fit_inside_vertically(self, value: Optional[bool]):
        self._set_attr("tooltipFitInsideVertically", value)

    # tooltip_fit_inside_horizontally
    @property
    def tooltip_fit_inside_horizontally(self) -> Optional[bool]:
        return self._get_attr(
            "tooltipFitInsideHorizontally", data_type="bool", def_value=False
        )

    @tooltip_fit_inside_horizontally.setter
    def tooltip_fit_inside_horizontally(self, value: Optional[bool]):
        self._set_attr("tooltipFitInsideHorizontally", value)

    # tooltip_show_on_top_of_chart_box_area
    @property
    def tooltip_show_on_top_of_chart_box_area(self) -> Optional[bool]:
        return self._get_attr(
            "tooltipShowOnTopOfChartBoxArea", data_type="bool", def_value=False
        )

    @tooltip_show_on_top_of_chart_box_area.setter
    def tooltip_show_on_top_of_chart_box_area(self, value: Optional[bool]):
        self._set_attr("tooltipShowOnTopOfChartBoxArea", value)

    # tooltip_border_side
    @property
    def tooltip_border_side(self) -> Optional[BorderSide]:
        return self.__tooltip_border_side

    @tooltip_border_side.setter
    def tooltip_border_side(self, value: Optional[BorderSide]):
        self.__tooltip_border_side = value

    # on_chart_event
    @property
    def on_chart_event(self) -> OptionalEventCallable["LineChartEvent"]:
        return self.__on_chart_event.handler

    @on_chart_event.setter
    def on_chart_event(self, handler: OptionalEventCallable["LineChartEvent"]):
        self.__on_chart_event.handler = handler
        self._set_attr("onChartEvent", True if handler is not None else None)


class LineChartEvent(ControlEvent):
    def __init__(self, e: ControlEvent):
        super().__init__(e.target, e.name, e.data, e.control, e.page)
        d = json.loads(e.data)
        self.type: str = d.get("type")
        self.spots: List[LineChartEventSpot] = d.get("spots")


class LineChartEventSpot:
    def __init__(self, bar_index, spot_index):
        self.bar_index: int = bar_index
        self.spot_index: int = spot_index
