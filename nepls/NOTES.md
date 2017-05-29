Measuring Reticulated Python
===

stages of grief
I am acceptance
most of you aren't even on "grief" so lets fix that right away

example well-typed programs
Retic is a sound gradual typing system

oakay lets backtrack


I. type soundness
- have PL, have eval, have proof system, check if its sound
- theorem has 3 clauses
- lets say you prove this, are successful. Who cares?
  why should Ron-programmer pick your sound language over an untyped language?
  - especially since, are real costs for doing so (annotations, reject good programs)
- conventional wisdom, three killer apps
  1. catch errors, eliminate class of bugs
  2. documentation
  3. speed, you and your compiler can trust the types
- this is type soundness you know and love,
  if you're not interested in typed languages then hope you can see how
   another programmer might want these properties
  (maybe you want them yourself just not at the price)
  the focus
  1. protect against errors
  2. compositional reasoning
   (once I understand f at top-level, I understand how it could be re-used)

2. gradual typing
origins depend who you ask
A. we live in multi-language world, fine-grained interop, type system for that interop
B. have untyped application, want to add benefits of static typing incrementally, software always evolving unexpectedly

3. gradual typing and type soundness, Part I
- cannot re=use standard soundness
- option I: generalize
  - add case for untyped code, everything else the same
  - typed code safe if typed code flows in,
    possibly-unsafe if untyped code flows in but that boundary is held accountable
  - untyped code just cannot mess with typed code
- nice properties
- heavy implementation, need proxies all the way down

3. GT and TS, Part II
- change conventional soundness
- v : \floor{t}

- hope you are enjoying grief, time for denial
- check the paper its really there, that's the soundness they write about

anger? depression? bargaining?
now is a good time for questions if you have any

4. why would anyone want this?
- easier to implement
- less to check dynamically
- performance numbers, compare 20-deliverable and 10-deliverable, and maybe max's

5. so wats' next? four questions
  1. retic useful
  2. TR fast
  3. TR portable
  4. gradual typing soundness, Part III

maybe you will be the one to propose Part III
