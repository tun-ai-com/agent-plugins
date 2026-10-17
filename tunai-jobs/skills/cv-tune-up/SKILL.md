---
name: cv-tune-up
description: Check and improve a CV or resume with TUNAI. Use when the user asks to check, review, score, improve or tailor their CV or resume, or to see how it fits a job.
---

# CV tune-up with TUNAI

The CV is read once by the tools and not kept. Only send a CV the user has asked you to check.

1. Call `check_cv_ats` with the CV text, the user's country as `market` (gb, us, ca or au) and the target role as `role` if they have
   one. List the failed checks, most important first, and the score.
2. Rewrite only what the checks flag, using the user's own facts. Never invent a job, a date, a qualification or a number. Show the
   changes and ask before replacing anything.
3. Call `check_cv_ats` again on the rewrite and report the score before and after.
4. If the user has a target job, find it with `search_jobs` (or take the pasted advert) and call `match_cv_to_job`. Report the
   skills the CV shows, the ones the job asks for that it does not, and which of those the user really has and should add.
5. To find jobs from the CV itself, call `find_jobs_for_cv`. Present the best five with their `fit` (strong or stretch), the
   `skills_not_in_your_cv` to add, and a link: the `source_url` when the job has one, otherwise its `apply_url` (a job with an
   `apply_url` has no TUNAI page and no `job_id`; to check the CV against it, paste its advert text as `job_description` to
   `match_cv_to_job`). Jobs marked `related_role` are close to an earlier post on the CV, not the role it points to: say so. If the
   notes say few jobs fit, tell the user that is the job board being thin for their kind of work, not a verdict on the CV.

If a tool says the model budget is used up for today, say so and continue with the checks that need no model.
