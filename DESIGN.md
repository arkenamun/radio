# Radio User Guide: design notes (v2.0 draft)

Training sheets for Shire of Denmark bush fire brigade members. Printed A4,
read in a hurry, often in a vehicle. The look is deliberately different from
the dScribe product sheets: those are a product; these are brigade training
material and may carry Shire and DFES branding.

## Look and feel

- **Light page, green rule, yellow tab.** No dark header. A bush-green rule
  under the title, and the sheet series shown as tabs top right with the
  current sheet in hi-vis yellow (the colour of BFB turnout gear).
- **Type.** Barlow Condensed for titles, numbers and prowords (reads like
  field signage, fits long words in narrow columns); Source Sans 3 for body
  text (humanist, highly legible at 9 pt, widely used in public-sector
  documents). Both are SIL Open Font Licence; the files are in `src/fonts/`.
- **Colour means something.** Green: how-to. Blue: things said on the radio.
  Orange and purple: the two issues on sheet 3. Red: the emergency message
  only. Yellow: the current sheet and the Talk-Around rule.
- **Radio phrases always look the same:** a speech-bubble bar with a speaker
  icon, prowords in bold. Example calls are a two-column dialogue with YOU in
  green.
- **Branding.** A text lockup, "Shire of Denmark · Bush Fire Brigades · WAERN
  radio", with a reserved slot for the Shire and DFES logos. The logos are
  not embedded: they are the organisations' marks and need their approval
  (DFES Social Media Policy; Shire P040111). Put them in once agreed.

## What changed in the content

- Sheet 1: each radio is a drawing with its keys labelled, next to a short
  task-by-task list. The Talk-Around rule, which both radios share, is stated
  once in a yellow box. The Denmark channel list is a table with chips for the
  radio that carries each channel.
- Sheet 2: the example call is a dialogue; "Moving off the command channel"
  and the prowords sit side by side; the emergency message is the only red
  item on the page and lists what to say in order.
- Sheet 3: the radio-shadow drawing is redrawn with labelled paths (relayed,
  blocked, Talk-Around); the signal-report chips are a single strip; the QR
  code to the example recordings is in the footer.

## Building

`src/radio-user-guide.html` is the source. Render with Playwright:

    python3 src/render.py radio-user-guide.html ../brads-radio-user-guide-a4-v2.0-draft.pdf
    python3 src/check.py radio-user-guide.html      # reports any page overflow

Sheet 3 alone: `qpdf --empty --pages guide.pdf 3 -- issues.pdf`.
