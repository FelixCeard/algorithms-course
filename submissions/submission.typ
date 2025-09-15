// #set columns(2)
#set page(columns: 1)
#for i in (1, 2, 3, 4) {
  pagebreak(weak: true)
  [= Schedule #i]
  // place(
    // top + center,
    // scope: "parent",
    // float: false,

  table(
    columns: (1fr, 1fr),
    stroke: none,
    [
    == Jobs
    \ 
    #let text = read("Job-" + str(i) + ".txt")
    #raw(text, lang: "html")
    ], 
    [
      == Optimal Assignment
      \
      #let text = read("Schedule-" + str(i) + ".txt")
      #raw(text, lang: "html")
    ]
  )
  // )
  // [= Schedule #i]
  // [== Jobs \ \ ]
  // let text = read("Job-" + str(i) + ".txt")
  // raw(text, lang: "html")
  // v(100%)
  // [\ ]
  // [== Optimal Assignment \ \ ]
  // let text = read("Schedule-" + str(i) + ".txt")
  // raw(text, lang: "html")
  // place(
  // top + center,
  // scope: "parent",
  // float: true,
  // // text(1.4em, weight: "bold")[
  //   // My document
  // // ],
  // [
  // // Red: Assignment; Blue: Job time window
  // ]
  // )
  // v(10%)
  place(
    bottom + center,
    float: true,
    scope: "parent",
    align(center, [
      #image("schedule" + str(i) + ".png", width: 95%)
    ])

  )

  // set columns(1)
}