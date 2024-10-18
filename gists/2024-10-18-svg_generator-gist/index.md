# 20241018-svg-generator

**Gist file**: [https://gist.github.com/athursto/bc0b9d46734a30dd3f6707e97e98b742](https://gist.github.com/athursto/bc0b9d46734a30dd3f6707e97e98b742)

**Description**: Cassidy's interview question of the week: a function to generate a valid SVG string for a circle given its radius, center position, and color.

## svg_generator.py

```Python

"""10.18.2024
Write a function that generates a valid SVG string for a circle given its radius, center position, and color.

"""

def generate_circle(radius, center, color):
    svg_string = f"<svg width='{center[0] * 2}' height ='{center[1] * 2}'><circle cx='{center[0]}' cy='{center[1]}' " \
             f"r='{radius}' fill='{color}'/></svg>"

    return svg_string

assert generate_circle(radius = 50, center = (100, 100), color = "blue") == \
       "<svg width='200' height ='200'><circle cx='100' cy='100' r='50' fill='blue'/></svg>"
```