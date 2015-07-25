data="""\
{{ id }}{
  background-color: {{ style.background }};
}

{{ id }}path,
{{ id }}line,
{{ id }}rect,
{{ id }}circle {
  -webkit-transition: {{ style.transition }};
  -moz-transition: {{ style.transition }};
  transition: {{ style.transition }};
}

{{ id }}.graph > .background {
  fill: {{ style.background }};
}

{{ id }}.plot > .background {
  fill: {{ style.plot_background }};
}

{{ id }}.graph {
  fill: {{ style.foreground }};
}

{{ id }}text.no_data {
  fill: {{ style.foreground_light }};
}

{{ id }}.title {
  fill: {{ style.foreground_light }};
}

{{ id }}.legends .legend text {
  fill: {{ style.foreground }};
}

{{ id }}.legends .legend:hover text {
  fill: {{ style.foreground_light }};
}

{{ id }}.axis .line {
  stroke: {{ style.foreground_light }};
}

{{ id }}.axis .guide.line {
  stroke: {{ style.foreground_dark }};
}

{{ id }}.axis .major.line {
  stroke: {{ style.foreground }};
}

{{ id }}.axis text.major {
  stroke: {{ style.foreground_light }};
  fill: {{ style.foreground_light }};
}

{{ id }}.axis.y .guides:hover .guide.line,
{{ id }}.line-graph .axis.x .guides:hover .guide.line,
{{ id }}.stackedline-graph .axis.x .guides:hover .guide.line,
{{ id }}.xy-graph .axis.x .guides:hover .guide.line {
  stroke: {{ style.foreground_light }};
}

{{ id }}.axis .guides:hover text {
  fill: {{ style.foreground_light }};
}

{{ id }}.reactive {
  fill-opacity: {{ style.opacity }};
}

{{ id }}.reactive.active,
{{ id }}.active .reactive {
  fill-opacity:  {{ style.opacity_hover }};
}

{{ id }}.series {
  stroke-width: {{ style.stroke_width }};
  stroke-linejoin: {{ style.stroke_style }};
  stroke-linecap: {{ style.stroke_style }};
  stroke-dasharray: {{ style.stroke_dasharray }};
}

{{ id }}.series text {
  fill: {{ style.foreground_light }};
}

{{ id }}.tooltip rect {
  fill: {{ style.plot_background }};
  stroke: {{ style.foreground_light }};
}

{{ id }}.tooltip text {
  fill: {{ style.foreground_light }};
}

{{ id }}.map-element {
  fill: {{ style.foreground }};
  stroke: {{ style.foreground_dark }} !important;
  opacity: .9;
  stroke-width: 3;
  -webkit-transition: 250ms;
  -moz-transition: 250ms;
  -o-transition: 250ms;
  transition: 250ms;
}

{{ id }}.map-element:hover {
  opacity: 1;
  stroke-width: 10;
}

{{ colors }}


"""