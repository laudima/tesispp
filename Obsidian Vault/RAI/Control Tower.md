I am building a business knowledge wiki using Obsidian and Claude.
The wiki will be maintained by an LLM — not by me. Every time new
source files arrive in my inbox folder, Claude will read them and
update the wiki automatically. The schema is the instruction manual
that tells Claude how the wiki is structured and what to do.

I need you to create a SCHEMA.md file for my wiki based on the
following information about my business:

BUSINESS DESCRIPTION

tech consulting principal product is 360 diagnostic wich offers you possible solutions to reduce the operative charge in your buisness 

MAIN ARTIFACT TYPES
meeting transcripts, 
client emails,
content briefs,
project docs  (html documents with information)
SOPs

MAIN ENTITY TYPES
projects
	diseño diagnostico 360
     diseño diagnostico rapido
     diseño de operacion del blue print
     control tower

team members
	Mauricio Pascal
	 Laura Itzel Rodriguez 


WIKI FOLDER STRUCTURE
/wiki/
├── index.md
├── log.md
├── /clients/
├── /projects/
├── /content/
├── /people/
├── /decisions/
└── /concepts/

---

Using this information, write a SCHEMA.md file that covers the
following sections:

1. OVERVIEW
A plain English description of what this wiki is, what it tracks,
and who maintains it. Two to three sentences. Written so that any
LLM reading it for the first time understands its role immediately.

2. PAGE TYPES
For each entity type, define:
- What this page tracks
- What sections it must always contain
- What optional sections it may contain
- Naming convention for the file
- Example filename

3. NAMING CONVENTIONS
Rules for how all files and folders are named. Keep it simple:
lowercase, hyphens not spaces, no special characters.

4. INGEST WORKFLOW
Step by step instructions for what to do when new source files
arrive. Written as a numbered list that Claude follows in order
every single time. Should cover: reading sources, identifying
entities, updating existing pages, creating new pages, updating
index.md, appending to log.md, outputting a summary.

5. INDEX FORMAT
The exact format for entries in index.md. Include an example entry.

6. LOG FORMAT
The exact format for entries in log.md including the prefix
pattern. Include an example entry.

7. CROSS-LINKING RULES
When to link between pages, how to format links, and what to do
when sources contradict each other.

8. RULES FOR THE LLM
A short list of standing instructions that apply to every session.
Things like: never copy-paste from sources, always read index.md
before starting, flag conflicts rather than silently resolving
them, do not create a page for something with only a name and no
other information.

---

Write the schema in clean markdown. Use headers and numbered or
bulleted lists throughout so it is easy to scan. The tone should
be direct and instructional — this is a reference document, not
prose. Every section should be specific enough that an LLM with
no prior context on this business could pick it up and maintain
the wiki correctly.