---
name: salary-check
description: Look up what a job pays and who is hiring with TUNAI. Use when the user asks what a role pays, how an offer compares, or which employers are hiring for a job title.
---

# Pay and hiring facts with TUNAI

1. Call `salary_for_role` with the role (and the city if the user gave one) and the country as `market`. Report the pay by level
   with the number of adverts behind each figure and the date it was measured. These are the pay adverts state, not what people are
   paid: say so.
2. Call `who_is_hiring` for the role to list the employers with the most live adverts. This is a count of open adverts, not growth
   or hiring intent.
3. For an offer, call `get_employer` for the employer and report its live jobs, how many are new this week, and how often its
   adverts state pay. Do not recommend an employer or an offer: give the facts and what to ask.
4. If a tool says there is too little data, report that. Never fill a gap with a number from your own memory.
