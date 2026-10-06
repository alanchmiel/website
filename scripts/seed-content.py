"""One-time content scaffold. Do not run after editing content: it overwrites files."""
from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
def write(name,meta,body):
 (root/'content'/name).write_text('---\n'+json.dumps(meta,indent=2,ensure_ascii=False)+'\n---\n\n'+body.strip()+'\n')
write('site.md',{'name':'Dr. Alan Chmiel','description':'Engineering, economics, and human behavior. Essays, research, and teaching on how consequential decisions take shape.','nav':[{'label':'Ideas','href':'/ideas/'},{'label':'Research','href':'/research/'},{'label':'Teaching','href':'/teaching/'},{'label':'About','href':'/about/'},{'label':'Speaking','href':'/speaking/'}],'homeLabel':'Home','skipLabel':'Skip to content','menuLabel':'Menu','closeMenuLabel':'Close menu','footerTitle':'Engineering the Decision','footerNote':'Personal writing and analysis. Views expressed are my own.','copyright':'© 2026 Dr. Alan Chmiel','ideasLabel':'Selected ideas','readLabel':'Read essay','backLabel':'All ideas','notFoundTitle':'This page could not be found','notFoundText':'Return to the homepage to explore the site.','contactLabel':'Get in touch','contactUrl':'','contactText':'For speaking, teaching, or research conversations, connect with me through my professional profile.','contactFallback':'https://www.linkedin.com/search/results/people/?keywords=Alan%20Chmiel','contactButton':'Find Alan on LinkedIn'},'')
write('home.md',{'title':'Engineering the Decision','eyebrow':'Engineering • Economics • Strategy','summary':'Where technology meets economics and human behavior.','ctaLabel':'Explore the ideas','ctaUrl':'/ideas/','secondaryLabel':'Meet Alan','secondaryUrl':'/about/'},'''# A better decision begins with a better question.

I study how technology, economics, and human behavior interact—and what that means for the decisions organizations and societies make.

## Possible ≠ Viable ≠ Adopted

A technology can work and still fail to create value or gain adoption. Those are different questions. Strategy begins by examining them together.

### What is possible?

Engineering establishes what can work: performance, reliability, interfaces, constraints, and failure modes.

### What is viable?

Economics examines value for the people involved: full costs, incentives, infrastructure, and the time horizon.

### What will be adopted?

Human behavior shapes what people choose and use: risk, habits, trust, and organizational routines.

## Experience meets inquiry.

My perspective connects engineering leadership, entrepreneurship, research, and teaching. I bring an engineer’s understanding of systems and a scholar’s attention to markets and behavior to the same question: **what should we do next?**

[Read my background](/about/)
''')
write('about.md',{'title':'About Alan','eyebrow':'Engineer • Executive • Researcher • Educator','summary':'A practical understanding of systems. A critical eye for assumptions.'},'''# Working across the boundaries of a decision.

I am Dr. Alan Chmiel, an engineer, executive, researcher, and educator based in Avon Lake, Ohio. My work examines how technical systems, economic conditions, and human behavior shape strategic choices.

## A perspective built in practice

I serve as Vice President of Engineering and Quality at R.W. Beckett Corporation. My background also includes aerospace leadership and medical device entrepreneurship. Across these settings, I have worked where reliability, innovation, and consequential decisions meet.

## Education

- **Doctor of Business Administration**, University of Pittsburgh, Katz Graduate School of Business
- **Master of Business Administration**, University of Wyoming
- **Bachelor of Science in Electrical Engineering**, University of Pittsburgh

My doctoral research focused on the economics of renewable liquid fuels. That work informs a broader interest in technology adoption, incentives, and the timing of energy transition.

## The question behind the work

Engineering tells us what is possible. Economics helps establish what is viable. Human behavior influences what is adopted. I use **Engineering the Decision** as an organizing lens for bringing those questions together.

I value arguments that make their assumptions visible, connect conclusions to evidence, and explain what would change the recommendation.
''')
write('research.md',{'title':'Research','eyebrow':'Markets • Incentives • Adoption','summary':'How do economic conditions and human behavior shape technology adoption?'},'''# The conditions between an idea and its use.

My research interests center on renewable liquid fuels, energy transition, consumer choice, and the economic conditions that shape adoption.

## Renewable liquid fuels

Renewable liquid fuels offer a way to examine the relationship between existing infrastructure and near-term emissions reductions. My doctoral work explores their economics, including the incentives and constraints affecting their use.

Questions include how policy signals enter market prices, how infrastructure affects the costs of transition, and how households evaluate changes to familiar systems.

## Timing and the time value of carbon

An emissions reduction today and a reduction years from now have different cumulative consequences. Evaluating a transition requires attention to timing as well as the eventual destination.

I am interested in how near-term options can complement longer-term changes, and how comparisons account for infrastructure, deployment speed, and adoption.

## Consumer choice and visibility

What people recall, notice, and perceive as risky can influence their choices. A technically capable solution may be difficult to observe, while a more visible change can carry signaling value.

These questions connect economic modeling with behavioral explanations of adoption.

## Research conversations

I welcome discussions about renewable fuel economics, technology adoption, and interdisciplinary approaches to energy transition.

[Background and credentials](/about/)
''')
write('teaching.md',{'title':'Teaching','eyebrow':'Concepts into practice','summary':'Real decisions make theory useful—and expose its assumptions.'},'''# Learn the model. Then examine the decision.

My teaching connects engineering, economics, technology, and organizational choices. Students begin with the people affected, the constraints they face, and the uncertainty surrounding the decision.

## A recurring approach

1. Define the decision and its alternatives.
2. Identify the technical requirements and supporting evidence.
3. Compare the full economic consequences.
4. Examine the assumptions about adoption and use.
5. Make a recommendation and explain what would change it.

## Areas of teaching

My teaching experience includes artificial intelligence and management information systems. Topics connect technology to implementation, organizational routines, incentives, and accountability.

## From an answer to an argument

A useful assignment asks students to compare a technically feasible solution with the economic and behavioral conditions needed for it to succeed. The final recommendation should identify assumptions, limits, and evidence to collect next.

The aim is judgment: knowing what a model explains, where it is incomplete, and how to act responsibly under uncertainty.
''')
write('speaking.md',{'title':'Speaking','eyebrow':'Ideas for consequential choices','summary':'Sessions that connect technical possibility with practical decisions.'},'''# Questions an audience can put to work.

I speak on the conditions between technical success and practical use, drawing on engineering, energy, organizational choices, and research on adoption.

## Engineering the Decision

A technology can work and still fail to create value or gain adoption. This session distinguishes feasibility, economic viability, and human adoption. Participants examine the assumptions they need to test before committing to a product, investment, or change initiative.

**For:** executive and interdisciplinary audiences.

## The Double Edged Heuristic

Experience helps us recognize patterns and make decisions quickly. It can also carry assumptions from yesterday’s environment into a different problem. This session examines how teams can use experience while testing its boundaries.

**For:** engineering and management teams.

## Energy Transition and the Time Value of Carbon

The timing of emissions reductions matters. This session considers how infrastructure, deployment speed, and adoption shape a comparison of near-term and longer-term transition options.

**For:** energy, industry, and policy audiences.

## Formats

A focused talk, a session with questions, or a workshop can be adapted to the audience’s decision. For an inquiry, include the audience, purpose, preferred format, timing, and the question you want participants to examine.
''')
write('ideas.md',{'title':'Ideas','eyebrow':'Engineering the Decision','summary':'Essays on the assumptions between technical success and practical use.'},'# Ideas worth examining.\n\nAn engineer’s questions. An economist’s tradeoffs. A practitioner’s attention to what happens next.')
write('ideas/why-the-best-technology-does-not-always-win.md',{'title':'Why the Best Technology Does Not Always Win','eyebrow':'Technology & adoption','summary':'Technical merit is one part of a decision. Costs, perceived risk, and disruption determine what happens next.','date':'2026-10-06','featured':True,'order':1},'''# Why the Best Technology Does Not Always Win

A technology can meet every engineering requirement and still struggle to find users. That does not make the engineering irrelevant. It tells us that the decision includes more than engineering.

## Three questions, three kinds of evidence

**Possible:** Can the technology perform reliably under the conditions that matter?

**Viable:** Does it create value for the people who must pay for it, maintain it, or depend on it?

**Adopted:** Will those people choose it, integrate it, and continue to use it?

A successful demonstration answers part of the first question. It does not settle the other two.

## Costs outside the comparison

An equipment comparison may capture purchase price and operating cost while overlooking training, integration, downtime, and the burden of changing a familiar process. Those costs may be difficult to quantify. They still influence the decision.

The relevant question is not simply whether the new system is better. It is whether the improvement is worth the transition for the person making the choice.

## The risk belongs to someone

A team proposing a change and a customer living with it may see different consequences. The team sees the performance gain. The customer may see a new dependency, a service question, or an interruption that comes at the wrong time.

Calling that response resistance can conceal useful information. It is often a prompt to investigate whose risk the comparison has omitted.

## Engineering the decision

Start with the technical case. Then ask who benefits, who bears the transition cost, and what must change for practical use. Specify the assumptions that matter and the evidence that would change the recommendation.

The best technology for a decision is the one whose capabilities, economics, and conditions of use fit the problem—not merely the one that leads a performance table.
''')
write('ideas/the-double-edged-heuristic.md',{'title':'The Double Edged Heuristic','eyebrow':'People & choice','summary':'Experience compresses complexity into useful rules. The challenge is recognizing when the environment has changed.','date':'2026-10-06','featured':True,'order':2},'''# The Double Edged Heuristic

Experience gives us shortcuts. We recognize a pattern, recall what happened last time, and act without rebuilding the entire analysis. In a familiar environment, that can be a considerable advantage.

## What experience carries

A heuristic often contains costs that a formal model misses: the supplier who needs additional follow-up, the installation that is rarely straightforward, or the customer who values service continuity more than a small efficiency gain.

These are useful observations. They deserve attention even when they are not neatly represented in a spreadsheet.

## What experience assumes

The same shortcut can preserve an old conclusion after its conditions have changed. A rule learned under a different cost structure, technology, or customer expectation may remain persuasive because it is familiar.

The danger is not having heuristics. It is treating them as evidence that cannot expire.

## Make the rule visible

Before accepting a judgment based on experience, ask:

- What recurring pattern produced this rule?
- Which costs or risks is it capturing?
- What needs to remain true for it to work?
- What observation would show that it needs revising?

A formal model and an experienced practitioner can challenge each other productively. The model exposes assumptions. The practitioner identifies missing consequences. Better decisions come from making both explicit.
''')
write('ideas/the-time-value-of-carbon.md',{'title':'The Time Value of Carbon','eyebrow':'Energy & transition','summary':'A transition comparison needs a timeline. The cumulative consequences depend on when reductions begin.','date':'2026-10-06','featured':True,'order':3},'''# The Time Value of Carbon

A transition is a sequence of decisions over time. Comparing only the final state can hide the consequences of the years spent getting there.

## Begin with the timeline

Two options may eventually reach a similar endpoint while producing different emissions along the way. One may deliver a smaller reduction sooner. Another may deliver a larger reduction after equipment, infrastructure, and adoption are in place.

The comparison needs both the magnitude of the reduction and the time required to realize it.

## Existing infrastructure is part of the decision

Installed systems shape the cost and pace of change. Their role should be evaluated directly: what can be improved now, what must be replaced, and what would prevent a near-term action from fitting a longer-term transition?

These questions require evidence about actual performance and lifecycle consequences. A label such as transitional or permanent does not answer them.

## Compare paths, not just destinations

A useful analysis states its baseline, time horizon, lifecycle boundaries, deployment assumptions, and adoption constraints. It also asks how sensitive the conclusion is to delays or changing conditions.

The practical question is what sequence of actions can reduce emissions under the conditions we face, while preserving the ability to improve as those conditions change.
''')
