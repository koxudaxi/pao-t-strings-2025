---
theme: seriph
background: https://source.unsplash.com/1920x1080/?python,code
title: 't-strings: Template Strings in Python 3.14'
info: |
  PEP 750 introduces template strings to Python 3.14, bringing
  structured text processing as a first-class language feature.
class: text-center
highlighter: shiki
lineNumbers: false
drawings:
  persist: false
transition: slide-left
mdc: true
fonts:
  sans: 'Lexend, sans-serif'
  mono: 'JetBrains Mono, monospace'
---

# t-strings <span class="text-yellow-400">(PEP 750)</span>

<div class="text-6xl font-bold mt-8">
  The Future of Python Templates
</div>

<div class="text-4xl font-bold mt-8 text-gray-300">
  Python 3.14
</div>

<div class="absolute bottom-10 left-0 right-0 text-center text-2xl font-semibold text-gray-400">
  PAO Charity Event 2025
</div>

<style>
  /* Global font improvements */
  .slidev-layout h1 {
    @apply text-5xl font-bold;
  }
  
  .slidev-layout h2 {
    @apply text-4xl font-bold;
  }
  
  .slidev-layout h3 {
    @apply text-3xl font-semibold;
  }
  
  .slidev-layout p, .slidev-layout div {
    @apply font-medium;
  }
  
  .slidev-layout code {
    @apply font-semibold;
  }
  
  /* Increase contrast for gray text */
  .text-gray-400 {
    @apply text-gray-300;
  }
  
  .text-gray-500 {
    @apply text-gray-400;
  }
  
  /* Prevent overflow */
  .slidev-layout {
    @apply overflow-hidden;
  }
  
  /* Python REPL style */
  code .text-green-400 {
    @apply text-green-500 font-semibold;
  }
  
  /* Enhance code blocks */
  .slidev-code {
    @apply text-lg;
  }
</style>


---
transition: fade
layout: center
---

# What are <span v-mark.underline.yellow>t-strings</span>?

<div class="mt-8">
  <div v-click class="text-center mb-6">
    <code class="text-8xl font-bold bg-gray-800 px-20 py-12 rounded-lg">t"Hello {name}"</code>
  </div>
  
  <div v-click class="text-center text-5xl font-bold mb-4">
    <span class="text-gray-300">↓</span>
  </div>
  
  <div v-click class="text-center">
    <div class="inline-block bg-yellow-900/20 border-4 border-yellow-400 px-16 py-8 rounded-lg">
      <div class="text-5xl font-bold mb-3">📦 Template object</div>
      <div class="text-3xl font-semibold text-gray-300">NOT a string!</div>
    </div>
  </div>
</div>

<div v-click class="mt-8 text-4xl font-bold text-center text-yellow-400">
  First step toward structured text
</div>

---
layout: two-cols
---

# Dissecting t-strings

<div class="mt-8">
  <div v-click class="text-4xl font-mono mb-8">
    <code v-mark.highlight.yellow class="text-5xl">t"Hello, {name}!"</code>
  </div>
</div>

<div v-click class="mt-12">

```python
>>> name = "world"
>>> template = t"Hello, {name}!"
>>> template
Template(strings=('Hello, ', '!'), 
         interpolations=(Interpolation(value='world', ...),))
```

</div>

::right::

<div class="pl-8">
  <div v-click class="mb-8">
    <div class="text-2xl mb-4 text-orange-400">📝 Static Parts</div>
    <div class="bg-orange-900/20 p-4 rounded text-xl">
      <div>strings = (</div>
      <div class="pl-4">'Hello, ',</div>
      <div class="pl-4">'!'</div>
      <div>)</div>
    </div>
  </div>
  
  <div v-click>
    <div class="text-2xl mb-4 text-blue-400">🔗 Dynamic Parts</div>
    <div class="bg-blue-900/20 p-4 rounded text-xl">
      <div>interpolations = (</div>
      <div class="pl-4">Interpolation(</div>
      <div class="pl-8">value='world',</div>
      <div class="pl-8">expression='name'</div>
      <div class="pl-4">),</div>
      <div>)</div>
    </div>
  </div>
</div>

---
layout: two-cols
---

# About Me

<div class="text-2xl space-y-6">
  <div v-click>
    <div class="text-3xl text-yellow-400 font-bold">Koudai Aono</div>
    <div class="text-2xl text-gray-300">@koxudaxi</div>
  </div>
  
  <div v-click>
    <div class="text-2xl text-white">🏢 OSS Developer at Mirascope</div>
  </div>
  
  <div v-click>
    <div class="text-2xl text-white">🔧 My OSS Projects</div>
    <div class="text-xl text-gray-300 ml-6">• PyCharm plugins for Pydantic & Ruff</div>
    <div class="text-xl text-gray-300 ml-6">• datamodel-code-generator</div>
  </div>
  
  <div v-click>
    <div class="text-2xl text-white">✨ PEP 750 Co-author</div>
    <div class="text-xl text-gray-300 ml-6">Template strings 🎉 - Python 3.14</div>
  </div>
  
  <div v-click>
    <div class="text-2xl text-white">🎤 Speaker</div>
    <div class="text-xl text-gray-300 ml-6">PyCon US 2024, 2025</div>
    <div class="text-xl text-gray-300 ml-6">EuroPython 2024, 2025</div>
  </div>
</div>

::right::

<div class="flex flex-col items-center justify-center h-full">
  <div v-click class="mb-8">
    <img src="/assets/profile.jpg" class="w-64 h-48 object-cover rounded-lg" alt="Profile" />
  </div>
  
  <div v-click>
    <div class="bg-white p-2 rounded">
      <img src="/assets/qrcode_github.svg" class="w-48" alt="GitHub QR Code" />
    </div>
  </div>
</div>

---
layout: center
transition: fade
---

# Talk Agenda

<div class="grid grid-cols-2 gap-6 mt-8">
  <div v-click class="bg-gray-800 p-6 rounded-lg">
    <div class="text-5xl mb-3">🤔</div>
    <div class="text-xl font-bold mb-1">Motivation</div>
    <div class="text-sm text-gray-400">Why do we need t-strings?</div>
  </div>
  
  <div v-click class="bg-gray-800 p-6 rounded-lg">
    <div class="text-5xl mb-3">⚙️</div>
    <div class="text-xl font-bold mb-1">How it Works</div>
    <div class="text-sm text-gray-400">Template & Interpolation types</div>
  </div>
  
  <div v-click class="bg-gray-800 p-6 rounded-lg">
    <div class="text-5xl mb-3">💡</div>
    <div class="text-xl font-bold mb-1">Real Examples</div>
    <div class="text-sm text-gray-400">SQL, HTML, Logging & more</div>
  </div>
  
  <div v-click class="bg-gray-800 p-6 rounded-lg">
    <div class="text-5xl mb-3">🚀</div>
    <div class="text-xl font-bold mb-1">Building the Future</div>
    <div class="text-sm text-gray-400">Ecosystem & community</div>
  </div>
</div>

---
layout: section
transition: slide-up
---

<h1 class="text-6xl">Part 1</h1>
<h2 class="text-5xl mt-4"><span class="text-yellow-400">Motivation</span></h2>

---

# Evolution of String Formatting

<div class="text-4xl leading-relaxed">
  <div v-click class="mb-6">
    <code class="text-gray-500">"%s" % name</code>
    <span class="ml-8 text-2xl text-gray-600">C-style</span>
  </div>
  
  <div v-click class="mb-6">
    <code class="text-gray-400">"{}".format(name)</code>
    <span class="ml-8 text-2xl text-gray-600">More flexible</span>
  </div>
  
  <div v-click class="mb-6">
    <code class="text-gray-300">f"{name}"</code>
    <span class="ml-8 text-2xl text-gray-600">Readable & fast</span>
  </div>
  
  <div v-click class="mt-12 text-yellow-400">
    <code v-mark.highlight.yellow>t"{name}"</code>
    <span class="ml-8 text-2xl">What's next?</span>
  </div>
</div>

---
layout: center
---

# The Security Problem

<div class="text-5xl mt-10 mb-10">
  🚨 <span class="text-red-500">SQL Injection</span> 🚨
</div>

<div v-click class="bg-red-900/20 p-8 rounded-lg border-2 border-red-500">
  <div class="text-3xl font-mono mb-4">
    <span class="text-gray-300">f"SELECT * FROM users WHERE id = </span><span v-mark.circle.red="2">{user_id}</span><span class="text-gray-300">"</span>
  </div>
  <div v-click="3" class="text-2xl text-red-400 mt-4">
    user_id = "1; DROP TABLE users; --"
  </div>
</div>

<div v-click class="text-4xl mt-12 text-center">
  💥 Database destroyed! 💥
</div>

---

# XSS Vulnerability

<div class="text-3xl font-mono mb-8">
  <span class="text-gray-300">f"&lt;h1&gt;Welcome </span><span v-mark.highlight.red>{username}</span><span class="text-gray-300">&lt;/h1&gt;"</span>
</div>

<div v-click class="bg-red-900/20 p-6 rounded-lg mb-8">
  <div class="text-2xl mb-4">If username contains:</div>
  <code class="text-xl text-red-400">&lt;script&gt;alert('hacked!')&lt;/script&gt;</code>
</div>

<div v-click class="text-center">
  <div class="text-6xl mb-4">⚡</div>
  <div class="text-3xl text-red-500">JavaScript executes!</div>
  <div class="text-2xl text-gray-400 mt-4">User data becomes code</div>
</div>

---

# Current Limitations

<div class="grid grid-cols-2 gap-12 mt-12">
  <div v-click>
    <div class="text-4xl mb-4">🚫 No Pre-processing</div>
    <div class="text-xl text-gray-400">
      Can't intercept values before they're combined
    </div>
  </div>
  
  <div v-click>
    <div class="text-4xl mb-4">🔍 No Analysis</div>
    <div class="text-xl text-gray-400">
      Lost context after evaluation
    </div>
  </div>
  
  <div v-click>
    <div class="text-4xl mb-4">🤷 No Safety</div>
    <div class="text-xl text-gray-400">
      Mix structure and data unsafely
    </div>
  </div>
  
  <div v-click>
    <div class="text-4xl mb-4">📋 No Structure</div>
    <div class="text-xl text-gray-400">
      Just produces plain strings
    </div>
  </div>
</div>

---
layout: center
---

# The Sub-language Challenge

<div v-click class="text-3xl mb-12">
  Templates contain <span class="text-yellow-400">fragmented sub-languages</span>
</div>

<div v-click class="grid grid-cols-2 gap-8">
  <div class="bg-gray-800 p-6 rounded">
    <div class="text-xl mb-4 text-blue-400">SQL fragments</div>
    <code class="text-sm">
      SELECT * FROM {table}<br>
      WHERE {conditions}<br>
      ORDER BY {sort}
    </code>
  </div>
  
  <div class="bg-gray-800 p-6 rounded">
    <div class="text-xl mb-4 text-green-400">HTML fragments</div>
    <code class="text-sm">
      &lt;div class="{classes}"&gt;<br>
      &nbsp;&nbsp;{content}<br>
      &lt;/div&gt;
    </code>
  </div>
</div>

<div v-click class="mt-12 text-2xl text-center">
  👀 <span class="text-red-400">Hard to validate visually</span><br>
  🔧 <span class="text-yellow-400">Libraries must parse & assemble</span><br>
  🎟️ <span class="text-green-400">Tools become very helpful</span>
</div>

---
layout: center
---

# What We Really Need

<div class="text-4xl space-y-6 mt-10">
  <div v-click class="flex items-center justify-center">
    <span class="text-8xl mr-6">🎯</span>
    <span>Structured text as <span class="text-yellow-400">first-class</span></span>
  </div>
  
  <div v-click class="flex items-center justify-center">
    <span class="text-8xl mr-6">🎉</span>
    <span>Separate <span class="text-blue-400">template</span> from <span class="text-green-400">values</span></span>
  </div>
  
  <div v-click class="flex items-center justify-center">
    <span class="text-8xl mr-6">🛡️</span>
    <span>Type-aware & <span class="text-red-400">safe</span></span>
  </div>
</div>

---
layout: section
transition: slide-up
---

<h1 class="text-6xl">Part 2</h1>
<h2 class="text-5xl mt-4"><span class="text-yellow-400">How t-strings Work</span></h2>

---
transition: slide-left
---

# Basic Syntax

<div class="grid grid-cols-2 gap-8 mt-8">
  <div v-click>
    <div class="text-2xl mb-4 text-red-400">f-string</div>
    <div class="bg-gray-800 p-6 rounded text-2xl">
      <code>>>> name = "world"</code><br>
      <code>>>> text = <span v-mark.underline.red="2">f"Hello {name}"</span></code><br>
      <code>>>> text</code><br>
      <code class="text-green-400">'Hello world'</code>
    </div>
  </div>
  
  <div v-click>
    <div class="text-2xl mb-4 text-green-400">t-string</div>
    <div class="bg-gray-800 p-6 rounded text-2xl">
      <code>>>> name = "world"</code><br>
      <code class="whitespace-nowrap">>>> template = <span v-mark.underline.green>t"Hello {name}"</span></code><br>
      <code>>>> template</code><br>
      <code class="text-green-400">Template(...)</code>
    </div>
  </div>
</div>

<div v-click class="text-center mt-12">
  <div class="text-4xl text-yellow-400">Same syntax, different result!</div>
  <div class="text-2xl mt-4 text-gray-400">String vs Template object</div>
</div>

---

# The Template Type

<div class="text-center mb-8">
  <code v-mark.box.orange class="text-4xl font-bold">t"Hello {name}!"</code>
</div>

<div v-click class="grid grid-cols-2 gap-8">
  <div class="bg-orange-900/20 border-2 border-orange-400 p-6 rounded-lg">
    <div class="text-2xl mb-4 text-orange-400 font-bold">.strings</div>
    <div class="text-xl space-y-2">
      <div>tuple[str, ...]</div>
      <div class="text-gray-400">Static parts</div>
      <code class="text-lg block mt-4">
        ("Hello ", "!")
      </code>
    </div>
  </div>
  
  <div class="bg-blue-900/20 border-2 border-blue-400 p-6 rounded-lg">
    <div class="text-2xl mb-4 text-blue-400 font-bold">.interpolations</div>
    <div class="text-xl space-y-2">
      <div>tuple[Interpolation, ...]</div>
      <div class="text-gray-400">Dynamic parts</div>
      <code class="text-lg block mt-4">
        (Interpolation(...),)
      </code>
    </div>
  </div>
</div>

<div v-click class="text-center mt-8">
  <div class="text-3xl font-bold text-yellow-400 mb-4">Pattern: str → interp → str → interp → ... → str</div>
  <div class="text-2xl text-gray-300">
    • Always starts and ends with a string<br>
    • Strings and interpolations alternate<br>
    • Therefore: len(strings) = len(interpolations) + 1
  </div>
</div>

---
layout: center
---

# The Interpolation Type

<div class="bg-gray-800 p-4 rounded-lg text-center">
  <code v-mark.underline.blue class="text-2xl font-bold">t"Hello {name:>10s}!"</code>
</div>

<div v-click class="mt-4 space-y-3">
  <div class="flex items-center">
    <div class="w-40 text-right mr-6 text-yellow-400 font-bold text-lg">value</div>
    <div class="text-2xl">"world"</div>
    <div class="ml-6 text-gray-500 text-base">← evaluated result</div>
  </div>
  
  <div v-click class="flex items-center">
    <div class="w-40 text-right mr-6 text-blue-400 font-bold text-lg">expression</div>
    <div class="text-2xl">"name"</div>
    <div class="ml-6 text-gray-500 text-base">← original code</div>
  </div>
  
  <div v-click class="flex items-center">
    <div class="w-40 text-right mr-6 text-green-400 font-bold text-lg">conversion</div>
    <div class="text-2xl">None</div>
    <div class="ml-6 text-gray-500 text-base">← !r, !s, !a</div>
  </div>
  
  <div v-click class="flex items-center">
    <div class="w-40 text-right mr-6 text-purple-400 font-bold text-lg">format_spec</div>
    <div class="text-2xl">">10s"</div>
    <div class="ml-6 text-gray-500 text-base">← after :</div>
  </div>
</div>

<div v-click class="mt-6 text-center">
  <div class="bg-red-900/20 border-2 border-red-400 px-6 py-3 rounded-lg inline-block">
    <div class="text-xl font-bold text-red-400">⚠️ NOT formatted yet!</div>
    <div class="text-lg text-gray-300 mt-1">Format specs are stored but not applied</div>
    <div class="text-lg text-gray-400 mt-1">Templates decide how to use them</div>
  </div>
</div>

---

# Evaluation Model

<div class="text-2xl space-y-6 mt-8">
  <div v-click>
    <div class="text-yellow-400 font-bold mb-2">⏰ Eager Evaluation</div>
    <div class="text-xl text-gray-400">Just like f-strings - no implicit lambdas</div>
  </div>
  
  <div v-click>
    <div class="text-blue-400 font-bold mb-2">🎯 Lexical Scoping</div>
    <div class="text-xl text-gray-400">Access to local and global variables</div>
  </div>
  
  <div v-click>
    <div class="text-green-400 font-bold mb-2">🐍 Full Python</div>
    <div class="text-xl text-gray-400">Any valid Python expression works</div>
  </div>
</div>

<div v-click class="mt-8 bg-gray-800 p-4 rounded-lg">
  <code class="text-xl">
    >>> x = 42<br>
    >>> template = <span v-mark.highlight.purple>t"Result: {x * 2 + 1}"</span><br>
    >>> template.interpolations[0].value<br>
    <span class="text-green-400">85</span>  <span class="text-gray-500"># ← Already evaluated!</span>
  </code>
</div>

<div v-click class="mt-6 text-center">
  <div class="bg-orange-900/20 border-2 border-orange-400 px-6 py-3 rounded-lg inline-block">
    <div class="text-xl font-bold text-orange-400">⚡ Immediate evaluation</div>
    <div class="text-lg text-gray-300 mt-1">NOT lazy - expressions are evaluated when template is created</div>
  </div>
</div>

---

# Template API Overview

<div class="grid grid-cols-2 gap-6 mt-4">
  <div v-click>
    <div class="text-2xl text-yellow-400 mb-2 font-bold">🔄 Iteration</div>
    <div class="bg-gray-800 p-3 rounded text-sm">
      <code>
        for item in template:<br>
        &nbsp;&nbsp;if isinstance(item, str):<br>
        &nbsp;&nbsp;&nbsp;&nbsp;# Static string part<br>
        &nbsp;&nbsp;else:<br>
        &nbsp;&nbsp;&nbsp;&nbsp;# Interpolation object
      </code>
    </div>
    <div class="text-xs text-gray-400 mt-2">Empty strings are omitted</div>
  </div>
  
  <div v-click>
    <div class="text-2xl text-blue-400 mb-2 font-bold">📦 Quick Access</div>
    <div class="bg-gray-800 p-3 rounded text-sm">
      <code>
        template.strings   # ('Hello ', '!')<br>
        template.values    # ('world',)<br>
        template.interpolations  # tuple[Interpolation, ...]
      </code>
    </div>
  </div>
  
  <div v-click>
    <div class="text-2xl text-green-400 mb-2 font-bold">➕ Concatenation</div>
    <div class="bg-gray-800 p-3 rounded text-sm">
      <code>
        <span class="text-green-400">t"Hello " + t"{name}"</span>  # ✓ Works!<br>
        <span class="text-green-400">t"Hello " t"{name}"</span>    # ✓ Implicit concat<br>
        <span class="text-red-400">t"Hello " + "world"</span>    # ✗ Error!
      </code>
    </div>
  </div>
  
  <div v-click>
    <div class="text-2xl text-purple-400 mb-2 font-bold">🐛 Debug Specifier</div>
    <div class="bg-gray-800 p-3 rounded text-sm">
      <code>
        t"Result: {value=}"<br>
        # → "Result: value=" + repr(value)<br>
        t"Result: {value=:.2f}"<br>
        # → "Result: value=" + format(value, '.2f')
      </code>
    </div>
  </div>
</div>

---

# Interpolation Object Details

<div class="grid grid-cols-2 gap-8 mt-6">
  <div v-click>
    <div class="bg-gradient-to-br from-blue-900/20 to-blue-800/10 p-6 rounded-xl border border-blue-400/30">
      <div class="text-2xl font-bold text-blue-400 mb-4">Core Attributes</div>
      <div class="space-y-3 text-lg">
        <div><code class="text-yellow-400">value</code>: The evaluated result</div>
        <div><code class="text-green-400">expression</code>: Original source code</div>
        <div><code class="text-orange-400">conversion</code>: "r", "s", "a", or None</div>
        <div><code class="text-purple-400">format_spec</code>: Format string after :</div>
      </div>
    </div>
  </div>
  
  <div v-click>
    <div class="bg-gradient-to-br from-green-900/20 to-green-800/10 p-6 rounded-xl border border-green-400/30">
      <div class="text-2xl font-bold text-green-400 mb-4">Example</div>
      <code class="text-sm">
        name = "Alice"<br>
        t = t"Hello {name!r:>10}"<br><br>
        interp = t.interpolations[0]<br>
        # interp.value == "Alice"<br>
        # interp.expression == "name"<br>
        # interp.conversion == "r"<br>
        # interp.format_spec == ">10"
      </code>
    </div>
  </div>
</div>

<div v-click class="mt-6 text-center bg-gray-800/50 p-4 rounded-lg">
  <div class="text-xl font-semibold text-yellow-400">💡 Key Point</div>
  <div class="text-lg text-gray-300 mt-2">
    Templates don't apply conversions or formatting - that's up to the processor!
  </div>
</div>

---

# Processing Templates with Pattern Matching

```python {class="text-xs"}
def process_template(template: Template) -> str:
    result = []
    for part in template:
        match part:
            case str():
                result.append(part)  # Static string part
            case Interpolation(value=val, conversion=conv, format_spec=spec):
                # Apply conversion
                if conv == "r": val = repr(val)
                elif conv == "s": val = str(val)
                elif conv == "a": val = ascii(val)
                # Apply format spec
                if spec: val = format(val, spec)
                else: val = str(val)
                result.append(val)
    return ''.join(result)
```

<div v-click class="mt-2 text-center">
  <div class="text-base font-bold text-yellow-400">Templates are structured data - Process them however you need!</div>
</div>

---
layout: section
transition: slide-up
---

<h1 class="text-6xl">Part 3</h1>
<h2 class="text-5xl mt-4"><span class="text-yellow-400">Real-World Examples</span></h2>

---
transition: slide-left
---

# Safe SQL with sql-tstring

<div class="text-xl text-gray-400 mb-8">Library by pgjones</div>

<div v-click class="bg-gray-800 p-6 rounded-lg mb-8">
  <code class="text-2xl">
    from sql_tstring import sql<br><br>
    user_id = "1; DROP TABLE users;"<br>
    query = sql(<span v-mark.underline.green>t"SELECT * FROM users WHERE id = {user_id}"</span>)<br>
  </code>
</div>

<div v-click class="grid grid-cols-2 gap-8">
  <div>
    <div class="text-2xl mb-4 text-green-400">✅ Result</div>
    <code class="text-lg">
      SELECT * FROM users WHERE id = ?<br>
      params = ['1; DROP TABLE users;']
    </code>
  </div>
  
  <div>
    <div class="text-2xl mb-4 text-yellow-400">🛡️ Benefits</div>
    <ul class="text-lg space-y-2">
      <li>Automatic parameterization</li>
      <li>Type-safe queries</li>
      <li>Injection prevention by design</li>
    </ul>
  </div>
</div>

---

# HTML Generation with tdom

<div v-click class="bg-gray-800 p-6 rounded-lg mb-8">
  <code class="text-xl">
    from tdom import html<br><br>
    user_input = "&lt;script&gt;alert('xss')&lt;/script&gt;"<br>
    safe_html = html(<span v-mark.underline.blue>t"&lt;h1&gt;{user_input}&lt;/h1&gt;"</span>)<br>
  </code>
</div>

<div v-click class="text-center my-8">
  <div class="text-3xl">↓</div>
</div>

<div v-click class="bg-green-900/20 p-6 rounded-lg">
  <code class="text-xl">
    &lt;h1&gt;&amp;lt;script&amp;gt;alert('xss')&amp;lt;/script&amp;gt;&lt;/h1&gt;
  </code>
</div>

<div v-click class="mt-8 text-2xl text-center">
  <span class="text-green-400">✨ Auto-escaped!</span>
  <span class="mx-4">•</span>
  <span class="text-blue-400">Context-aware</span>
  <span class="mx-4">•</span>
  <span class="text-yellow-400">No template engine</span>
</div>

---

# Structured Logging

<div v-click class="bg-gray-800 p-6 rounded-lg mb-8">
  <code class="text-xl">
    >>> action = "purchase"<br>
    >>> amount = 42.50<br>
    >>> logger.info(<span v-mark.highlight.orange>t"User {action}: ${amount:.2f}"</span>)<br>
  </code>
</div>

<div class="grid grid-cols-2 gap-8 mt-8">
  <div v-click>
    <div class="text-xl mb-4 text-blue-400">👥 Human Output</div>
    <div class="bg-gray-800 p-4 rounded">
      <code>User purchase: $42.50</code>
    </div>
  </div>
  
  <div v-click>
    <div class="text-xl mb-4 text-green-400">🤖 JSON Output</div>
    <div class="bg-gray-800 p-4 rounded">
      <code>
        {<br>
        &nbsp;&nbsp;"action": "purchase",<br>
        &nbsp;&nbsp;"amount": 42.50<br>
        }
      </code>
    </div>
  </div>
</div>

<div v-click class="text-center mt-8 text-2xl text-yellow-400">
  One template, multiple outputs!
</div>

---

# Flexible Use Cases

<div class="grid grid-cols-2 gap-6 mt-4">
  <div v-click>
    <div class="bg-gray-800 p-4 rounded-lg">
      <div class="text-xl mb-3 text-blue-400 font-bold">📧 Email Templates</div>
      <code class="text-sm">
        <span class="text-orange-400">template = t"""</span><br>
        Dear <span class="text-yellow-400">{user.name}</span>,<br>
        Your order #<span class="text-yellow-400">{order.id}</span><br>
        has been shipped!<br>
        <span class="text-orange-400">"""</span>
      </code>
    </div>
    <div v-click class="bg-blue-900/20 p-3 rounded-lg mt-3 border border-blue-400/30">
      <div class="text-sm font-semibold text-blue-400 mb-1">→ Result with custom processor:</div>
      <code class="text-xs text-gray-300">
        Dear Alice,<br>
        Your order #12345<br>
        has been shipped!
      </code>
    </div>
  </div>
  
  <div v-click>
    <div class="bg-gray-800 p-4 rounded-lg">
      <div class="text-xl mb-3 text-green-400 font-bold">⚙️ Config Files</div>
      <code class="text-sm">
        <span class="text-green-400">config = t"""</span><br>
        [database]<br>
        host = <span class="text-yellow-400">{db_host}</span><br>
        port = <span class="text-yellow-400">{db_port}</span><br>
        <span class="text-green-400">"""</span>
      </code>
    </div>
    <div v-click class="bg-green-900/20 p-3 rounded-lg mt-3 border border-green-400/30">
      <div class="text-sm font-semibold text-green-400 mb-1">→ Result with TOML processor:</div>
      <code class="text-xs text-gray-300">
        [database]<br>
        host = localhost<br>
        port = 5432
      </code>
    </div>
  </div>
</div>

<div v-click class="mt-6 text-center">
  <div class="text-xl font-bold text-yellow-400">Same template, different processors → different outputs!</div>
  <div class="text-lg text-gray-400 mt-2">Templates are data structures, not just strings</div>
</div>

---

# Why t-strings? Expanding Python's Horizons

## 🌍 Writing other languages in Python files becomes natural

<v-click>

**Before t-strings - Mixing languages felt awkward:**
```python
sql = "SELECT * FROM users WHERE id = " + str(user_id)  # 😱
js_code = "console.log('" + message + "')"  # 🤔
css = ".class-" + name + " { color: " + color + "; }"  # 😵
```

</v-click>

<v-click>

**With t-strings - Other languages feel like first-class citizens!**
```python
query = t"SELECT * FROM users WHERE id = {user_id}"  # ✨
js = t"console.log({message})"  # 🎯
css = t".class-{name} { color: {color}; }"  # 🚀
```

</v-click>

<v-click>

## 🚀 Opening new possibilities

**SQL has ORMs**, but what about...

<div class="grid grid-cols-2 gap-4">
  <div>
    <ul>
      <li><strong>CSS</strong> - Dynamic styles</li>
      <li><strong>JavaScript</strong> - Client-side logic</li>
      <li><strong>Shell</strong> - System commands</li>
    </ul>
  </div>
  <div>
    <ul>
      <li><strong>GraphQL</strong> - API queries</li>
      <li><strong>HTML</strong> - Dynamic markup</li>
      <li><strong>Your DSL!</strong> - Any language</li>
    </ul>
  </div>
</div>

</v-click>

---

# The Missing Piece: Sub-language Specification

<div class="text-center mt-4">
  <div v-click class="text-3xl font-bold text-red-400 mb-6">
    🤔 PEP 750 doesn't specify how to indicate sub-languages
  </div>
  
  <div v-click class="text-xl text-gray-300 space-y-3 mb-6">
    <div>• No built-in syntax like <code class="text-gray-500 line-through">t:sql"..."</code></div>
    <div>• No standard metadata mechanism</div>
    <div>• Left to the ecosystem to solve</div>
  </div>
  
  <div v-click class="bg-gray-800/50 p-5 rounded-xl inline-block">
    <div class="text-lg text-yellow-400 font-semibold mb-2">Current approaches:</div>
    <div class="text-base text-gray-300 space-y-2">
      <div>1. Type annotations: <code>Annotated[Template, "sql"]</code></div>
      <div>2. Naming conventions: <code>sql_template = t"..."</code></div>
      <div>3. Context inference: <code>db.execute(t"...")</code></div>
    </div>
  </div>
  
  <div v-click class="mt-6 text-lg text-gray-400">
    This is where tools like t-linter come in...
  </div>
</div>


---
layout: section
transition: slide-up
---

<h1 class="text-6xl">Part 4</h1>
<h2 class="text-5xl mt-4"><span class="text-yellow-400">Building the Future</span></h2>

---

# The Growing Ecosystem

<div class="grid grid-cols-2 gap-4 mt-4">
  <div v-click class="bg-gray-800 p-4 rounded-lg">
    <div class="text-xl mb-3 text-blue-400">📚 Libraries</div>
    <ul class="space-y-1 text-base">
      <li><span class="text-yellow-400">sql-tstring</span> - Safe SQL</li>
      <li><span class="text-yellow-400">tdom</span> - HTML generation</li>
      <li class="text-gray-500">More coming...</li>
    </ul>
  </div>
  
  <div v-click class="bg-gray-800 p-4 rounded-lg">
    <div class="text-xl mb-3 text-green-400">🔧 Tools</div>
    <ul class="space-y-1 text-base">
      <li><span class="text-yellow-400">t-linter</span> - My PoC</li>
      <li class="text-gray-500 ml-4">VSCode extension</li>
      <li class="text-gray-500 ml-4">PyCharm plugin</li>
    </ul>
  </div>
  
  <div v-click class="bg-gray-800 p-4 rounded-lg">
    <div class="text-xl mb-3 text-purple-400">🌐 Resources</div>
    <div class="flex items-center gap-4">
      <ul class="space-y-1 text-base">
        <li><span class="text-yellow-400">t-strings.help</span></li>
        <li><span class="text-yellow-400">awesome-t-strings</span></li>
      </ul>
      <div class="flex flex-col gap-2">
        <img src="/assets/qr-t-strings-help.png" class="w-14 h-14" alt="t-strings.help QR" />
        <img src="/assets/qr-awesome-t-strings.png" class="w-14 h-14" alt="awesome-t-strings QR" />
      </div>
    </div>
  </div>
  
  <div v-click class="bg-gray-800 p-4 rounded-lg">
    <div class="text-xl mb-3 text-red-400">🎯 Your Turn</div>
    <div class="text-base text-gray-400">
      Build something amazing!
    </div>
  </div>
</div>

---
layout: center
---

# Syntax Highlighting for Sub-languages

<div class="text-lg text-gray-400 mb-4">t-strings embed sub-languages directly in literals</div>

<div v-click class="mb-4">
  <img src="/assets/t-linter.png" class="mx-auto rounded-lg shadow-2xl max-w-2xl max-h-80 object-contain" alt="t-linter screenshot" />
</div>

<div v-click class="text-center space-y-2">
  <div class="text-xl font-bold text-yellow-400">t-linter: IDE Support for t-strings</div>
  <div class="text-lg text-gray-300">
    SQL syntax highlighting • HTML/CSS support • Extensible
  </div>
  <div class="text-base text-gray-400 mt-2">
    Working with the community to build the tooling ecosystem
  </div>
</div>

---

# t-linter Architecture

<div class="grid grid-cols-2 gap-12 mt-8">
  <div v-click>
    <div class="text-4xl font-bold text-yellow-400 mb-6 text-center">🦀 Built with Modern Tech</div>
    <div class="space-y-4 text-2xl">
      <div class="bg-gray-800/50 p-4 rounded-lg">
        <span class="text-orange-400 font-bold">Rust</span> for blazing performance
      </div>
      <div class="bg-gray-800/50 p-4 rounded-lg">
        <span class="text-blue-400 font-bold">Language Server Protocol</span>
        <div class="text-lg text-gray-400 mt-1">Works with any LSP-compatible editor</div>
      </div>
      <div class="bg-gray-800/50 p-4 rounded-lg text-center">
        <code class="text-xl px-4 py-2">pip install t-linter</code>
      </div>
    </div>
  </div>
  
  <div v-click>
    <div class="text-4xl font-bold text-green-400 mb-6 text-center">🌳 Powered by Tree-sitter</div>
    <div class="space-y-4">
      <div class="bg-gray-800/50 p-4 rounded-lg">
        <div class="text-2xl font-semibold">Incremental Parsing</div>
        <div class="text-lg text-gray-400">Updates only changed parts</div>
      </div>
      <div class="bg-gray-800/50 p-4 rounded-lg">
        <div class="text-2xl font-semibold">Battle-tested</div>
        <div class="text-lg text-gray-400">GitHub, Neovim, Emacs, Helix</div>
      </div>
      <div class="bg-gray-800/50 p-4 rounded-lg">
        <div class="text-2xl font-semibold">Multi-language Support</div>
        <div class="text-lg text-gray-400">HTML, SQL, JS, CSS, and more</div>
      </div>
    </div>
  </div>
</div>

---

# Editor Integration

<div class="grid grid-cols-2 gap-12 mt-8">
  <div v-click class="bg-gradient-to-br from-green-900/20 to-green-800/10 p-8 rounded-xl border-2 border-green-400/30">
    <div class="text-4xl font-bold text-green-400 mb-6 text-center">🔌 VSCode Extension</div>
    <div class="space-y-6">
      <div class="flex items-start gap-4">
        <span class="text-3xl">💡</span>
        <div>
          <div class="text-2xl font-semibold">Smart Highlighting</div>
          <div class="text-lg text-gray-400">Uses t-linter LSP server</div>
        </div>
      </div>
      <div class="flex items-start gap-4">
        <span class="text-3xl">🛍️</span>
        <div>
          <div class="text-2xl font-semibold">Easy Install</div>
          <div class="text-lg text-gray-400">Available on VSCode Marketplace</div>
        </div>
      </div>
      <div class="flex items-start gap-4">
        <span class="text-3xl">⚡</span>
        <div>
          <div class="text-2xl font-semibold">Real-time Detection</div>
          <div class="text-lg text-gray-400">Instant sub-language recognition</div>
        </div>
      </div>
    </div>
  </div>
  
  <div v-click class="bg-gradient-to-br from-yellow-900/20 to-yellow-800/10 p-8 rounded-xl border-2 border-yellow-400/30">
    <div class="text-4xl font-bold text-yellow-400 mb-6 text-center">🧩 PyCharm Plugin</div>
    <div class="space-y-6">
      <div class="flex items-start gap-4">
        <span class="text-3xl">🎯</span>
        <div>
          <div class="text-2xl font-semibold">Native Integration</div>
          <div class="text-lg text-gray-400">Multi-language injection</div>
        </div>
      </div>
      <div class="flex items-start gap-4">
        <span class="text-3xl">🔄</span>
        <div>
          <div class="text-2xl font-semibold">Same Experience</div>
          <div class="text-lg text-gray-400">Different tech, same result</div>
        </div>
      </div>
      <div class="flex items-start gap-4">
        <span class="text-3xl">🏗️</span>
        <div>
          <div class="text-2xl font-semibold">Built-in Features</div>
          <div class="text-lg text-gray-400">Leverages PyCharm's power</div>
        </div>
      </div>
    </div>
  </div>
</div>

<div v-click class="mt-12 text-center bg-gradient-to-r from-orange-600 to-red-600 py-6 rounded-xl">
  <div class="text-3xl font-bold text-white mb-2">🚀 Start Using t-linter Today!</div>
  <code class="text-2xl bg-black/30 px-8 py-3 rounded-lg text-white">pip install t-linter</code>
</div>

---

# Future Roadmap

<div class="text-center mb-4" v-click>
  <div class="text-4xl font-bold text-purple-400">🎯 What's Next for t-linter?</div>
</div>

<div class="grid grid-cols-2 gap-6 mt-6">
  <div v-click class="bg-gradient-to-br from-red-900/20 to-red-800/10 p-4 rounded-lg border border-red-400/30">
    <div class="flex items-start gap-3">
      <span class="text-3xl">✓</span>
      <div>
        <div class="text-2xl font-bold text-red-400">Syntax Validation</div>
        <div class="text-base text-gray-300 mt-1">
          Validate SQL, HTML, and more
        </div>
      </div>
    </div>
  </div>
  
  <div v-click class="bg-gradient-to-br from-blue-900/20 to-blue-800/10 p-4 rounded-lg border border-blue-400/30">
    <div class="flex items-start gap-3">
      <span class="text-3xl">📁</span>
      <div>
        <div class="text-2xl font-bold text-blue-400">Cross-file Types</div>
        <div class="text-base text-gray-300 mt-1">
          Track type aliases across files
        </div>
      </div>
    </div>
  </div>
  
  <div v-click class="bg-gradient-to-br from-green-900/20 to-green-800/10 p-4 rounded-lg border border-green-400/30">
    <div class="flex items-start gap-3">
      <span class="text-3xl">💡</span>
      <div>
        <div class="text-2xl font-bold text-green-400">Auto-completion</div>
        <div class="text-base text-gray-300 mt-1">
          Context-aware suggestions
        </div>
      </div>
    </div>
  </div>
  
  <div v-click class="bg-gradient-to-br from-yellow-900/20 to-yellow-800/10 p-4 rounded-lg border border-yellow-400/30">
    <div class="flex items-start gap-3">
      <span class="text-3xl">🔍</span>
      <div>
        <div class="text-2xl font-bold text-yellow-400">Diagnostics</div>
        <div class="text-base text-gray-300 mt-1">
          Real-time linting & checks
        </div>
      </div>
    </div>
  </div>
</div>

---
layout: center
---

# Language Hints Discussion

<div class="text-lg text-gray-400 mb-4">My proposal for template metadata</div>

<div v-click class="bg-gray-800 p-4 rounded-lg mb-4">
  <code class="text-base">
    from typing import Annotated<br>
    <br>
    def process_sql(tmpl: <span class="text-yellow-400">Annotated[Template, "sql"]</span>):<br>
    &nbsp;&nbsp;# IDE knows this is SQL<br>
    &nbsp;&nbsp;...<br>
    <br>
    process_sql(t"SELECT * FROM {table}")
  </code>
</div>

<div v-click class="text-lg space-y-2">
  <div>🎨 <span class="text-yellow-400">Better IDE support</span></div>
  <div>✅ <span class="text-green-400">Type checking</span></div>
  <div>🤖 <span class="text-blue-400">Smarter tooling</span></div>
</div>

<div v-click class="mt-4 flex items-center justify-center gap-8">
  <div class="text-center">
    <div class="text-base text-gray-400">Join the discussion!</div>
    <div class="text-base text-yellow-400">discuss.python.org/t/94311</div>
  </div>
  <img src="/assets/qr-language-hints.png" class="w-20 h-20" alt="QR code for discussion" />
</div>

---
layout: center
transition: slide-up
---

# Call to Action

<div class="text-3xl space-y-6 mt-8">
  <div v-click class="flex items-center justify-center">
    <span class="text-5xl mr-4">🧪</span>
    <span><span class="text-yellow-400">Try</span> the reference implementation</span>
  </div>
  
  <div v-click class="flex items-center justify-center">
    <span class="text-5xl mr-4">🏗️</span>
    <span><span class="text-green-400">Build</span> libraries for your use cases</span>
  </div>
  
  <div v-click class="flex items-center justify-center">
    <span class="text-5xl mr-4">🎆</span>
    <span><span class="text-blue-400">Share</span> on awesome-t-strings</span>
  </div>
  
  <div v-click class="flex items-center justify-center">
    <span class="text-5xl mr-4">👥</span>
    <span><span class="text-purple-400">Join</span> the discussion</span>
  </div>
</div>

---
layout: section
transition: slide-up
---

<h1 class="text-6xl">Closing</h1>

---
layout: center
transition: slide-up
---

# Key Takeaways

<div class="text-3xl space-y-6 mt-8">
  <div v-click>
    <span class="text-5xl mr-4">🎆</span>
    t-strings = <span class="text-yellow-400">structured text as first-class citizen</span>
  </div>
  
  <div v-click>
    <span class="text-5xl mr-4">🔒</span>
    <span class="text-green-400">Safety</span> through separation
  </div>
  
  <div v-click>
    <span class="text-5xl mr-4">🌱</span>
    <span class="text-blue-400">Growing ecosystem</span> needs you
  </div>
  
  <div v-click>
    <span class="text-5xl mr-4">🚀</span>
    <span class="text-purple-400">Future</span> is being written now
  </div>
</div>

---
layout: two-cols
transition: fade
---

# Let's Connect!

<div class="space-y-4 text-lg">
  <div>
    <div class="text-2xl font-bold text-yellow-400 mb-2">📄 Documentation</div>
    <div class="flex items-center gap-2">
      <div>t-strings.help</div>
      <img src="/assets/qr-t-strings-help.png" class="w-12 h-12" alt="QR" />
    </div>
    <div>PEP 750</div>
  </div>
  
  <div>
    <div class="text-2xl font-bold text-green-400 mb-2">💻 Resources</div>
    <div class="flex items-center gap-2">
      <div class="text-sm">github.com/t-strings/awesome-t-strings</div>
      <img src="/assets/qr-awesome-t-strings.png" class="w-12 h-12" alt="QR" />
    </div>
    <div class="flex items-center gap-2">
      <div class="text-sm">github.com/t-strings/tdom</div>
      <img src="/assets/qr-tdom.png" class="w-12 h-12" alt="QR" />
    </div>
    <div>pep750-examples repository</div>
  </div>
  
  <div>
    <div class="text-2xl font-bold text-blue-400 mb-2">🔧 Tools</div>
    <div class="flex items-center gap-2">
      <div class="text-sm">github.com/koxudaxi/t-linter</div>
      <img src="/assets/qr-t-linter-repo.png" class="w-12 h-12" alt="QR" />
    </div>
    <div class="flex items-center gap-2">
      <div class="text-sm">github.com/koxudaxi/t-linter-pycharm-plugin</div>
      <img src="/assets/qr-t-linter-pycharm.png" class="w-12 h-12" alt="QR" />
    </div>
  </div>
</div>

::right::

<div class="pl-8 space-y-4 text-lg">
  <div>
    <div class="text-2xl font-bold text-purple-400 mb-2">💬 Discussion</div>
    <div class="flex items-center gap-2">
      <div>discuss.python.org/t/94311</div>
      <img src="/assets/qr-language-hints.png" class="w-12 h-12" alt="QR" />
    </div>
  </div>
  
  <div>
    <div class="text-2xl font-bold text-red-400 mb-2">👨‍💻 Contact</div>
    <div>GitHub: @koxudaxi</div>
  </div>
  
  <div class="mt-8">
    <div class="bg-white p-2 rounded inline-block">
      <img src="/assets/qrcode_github.svg" class="w-48" alt="GitHub QR" />
    </div>
  </div>
</div>

<div class="absolute bottom-6 left-0 right-0 text-center text-2xl font-semibold text-gray-300">
  Thank you! Questions?
</div>
