
#let section-card(title, color: rgb("#1e40af"), content) = [
  #block(
    width: 100%,
    stroke: 0.75pt + color.lighten(50%),
    radius: 4pt,
    fill: white,
    inset: 0pt,
    outset: 0pt,
    clip: true,
    [
      #block(
        width: 100%,
        fill: color,
        inset: (x: 7pt, y: 4pt),
        text(weight: "bold", size: 8.5pt, fill: white)[#title]
      )
      #block(
        width: 100%,
        inset: (x: 7pt, top: 4.5pt, bottom: 4.5pt),
        content
      )
    ]
  )
  #v(4pt)
]

#let callout(title: "", color: rgb("#0f766e"), content) = [
  #block(
    width: 100%,
    fill: color.lighten(94%),
    stroke: (left: 3pt + color, rest: 0.5pt + color.lighten(70%)),
    radius: (right: 3pt),
    inset: (x: 6pt, y: 4pt),
    [
      #if title != "" [
        #text(weight: "bold", size: 7.8pt, fill: color)[#title]       ]
      #text(size: 7.5pt)[#content]
    ]
  )
  #v(2pt)
]

#section-card("Test Card")[
  #callout(title: "Important")[This is inside callout]
]
