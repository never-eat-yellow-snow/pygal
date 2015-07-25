data = """\
{{ id }}.title {
  font-family: "{{ style.font_family }}";
  font-size: {{ font_sizes.title }};
}

{{ id }}.legends .legend text {
  font-family: "{{ style.font_family }}";
  font-size: {{ font_sizes.legend }};
}

{{ id }}.axis text {
  font-family: "{{ style.font_family }}";
  font-size: {{ font_sizes.label }};
}

{{ id }}.axis text.major {
  font-family: "{{ style.font_family }}";
  font-size: {{ font_sizes.major_label }};
}

{{ id }}.series text {
  font-family: "{{ style.font_family }}";
  font-size: {{ font_sizes.value }};
}

{{ id }}.tooltip text {
  font-family: "{{ style.font_family }}";
  font-size: {{ font_sizes.tooltip }};
}

{{ id }}text.no_data {
  font-size: {{ font_sizes.no_data }};
}
"""