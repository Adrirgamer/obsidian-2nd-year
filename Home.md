---
cssclasses:
  - terminal-dashboard
---

# SCHOOL DASHBOARD
> [!info] Current Overview

```dataviewjs
// ======================================================
// LOAD DATA
// ======================================================

const subjectsPage = dv.page("Subjects.md");
const marksPage = dv.page("Marks.md");
const tasksPage = dv.page("Tasks.md");

let validSubjects = [];

if (subjectsPage?.file?.lists) {
    validSubjects = subjectsPage.file.lists.map(l =>
        l.text.replace(/^-\s*/, "").trim()
    );
}

let allMarks = [];

if (marksPage?.file?.lists) {
    allMarks = marksPage.file.lists.where(
        l =>
            l.assignment &&
            l.grade != null &&
            l.max != null &&
            l.subject
    );
}

if (validSubjects.length) {
    allMarks = allMarks.where(m =>
        validSubjects.includes(m.subject)
    );
}

let allTasks = [];

if (tasksPage?.file?.tasks) {
    allTasks = tasksPage.file.tasks.sort(
        t => t.due ? t.due.ts : 999999999999,
        "asc"
    );
}

const subjects = ["All", ...new Set(allMarks.map(m => m.subject))];

// ======================================================
// STATS
// ======================================================

let totalGrade = 0;
let totalMax = 0;

let rankingSum = 0;
let rankingCount = 0;

allMarks.forEach(m => {
    totalGrade += Number(m.grade);
    totalMax += Number(m.max);

    if (m.rank != null) {
        rankingSum += Number(m.rank);
        rankingCount++;
    }
});

const average =
    totalMax > 0
        ? ((totalGrade / totalMax) * 20).toFixed(2)
        : "0.00";

const avgRank =
    rankingCount > 0
        ? (rankingSum / rankingCount).toFixed(1)
        : "—";

const completedTasks =
    allTasks.filter(t => t.completed).length;

const completion =
    allTasks.length
        ? Math.round((completedTasks / allTasks.length) * 100)
        : 0;

// ======================================================
// STATE
// ======================================================

let activeSubject = "All";
const root = dv.el("div", "");

// ======================================================
// RENDER
// ======================================================

function render() {

    const marks =
        activeSubject === "All"
            ? allMarks
            : allMarks.where(m => m.subject === activeSubject);

    let html = "";

    // ==================================================
    // CRAB ANIMATION (PIXEL OVERLAY)
    // ==================================================

    html += `
<div class="jumping-dots">
  <span></span><span></span><span></span>
</div>
<div class="pixel-bar top"></div>
<div class="pixel-bar bottom"></div>
`;

    // ==================================================
    // TOP STATS
    // ==================================================

    html += `
<div class="dashboard-section">

<div class="top-stats">

<div class="avg-circle">
    <div class="value">${average}</div>
    <div class="stat-label">Avg /20</div>
</div>

<div class="rank-box">
    <div class="value">${avgRank}</div>
    <div class="stat-label">Rank</div>
</div>

</div>

<div class="stat-grid">
    <div class="stat-card">
        <h3>${allTasks.length}</h3>
        Tasks
    </div>

    <div class="stat-card">
        <h3>${completion}%</h3>
        Done
    </div>

    <div class="stat-card">
        <h3>${subjects.length - 1}</h3>
        Subjects
    </div>
</div>

</div>
`;

    // ==================================================
    // MAIN GRID
    // ==================================================

    html += `<div class="dashboard-section main-grid">`;

    // --------------------------------------------------
    // SUBJECTS (FORCED TOP ROW)
    // --------------------------------------------------

    html += `
<div class="subjects-row">

<h2>Subjects</h2>

<div class="tabs">
`;

    subjects.forEach(sub => {
        html += `
<span class="tab-label ${activeSubject === sub ? "active" : ""}"
onclick="this.dispatchEvent(new CustomEvent('changeSubject',{bubbles:true,detail:'${sub}'}))">
${sub}
</span>`;
    });

    html += `
</div>

</div>
`;

    // --------------------------------------------------
    // PROGRESSION
    // --------------------------------------------------

    html += `
<div>

<h2>${activeSubject} Progression</h2>

<div class="chart-container">
`;

    [...marks].slice(-20).forEach(m => {

        const pct = (Number(m.grade) / Number(m.max)) * 100;

        let barClass = "bar-bad";
        if (pct >= 70) barClass = "bar-good";
        else if (pct >= 50) barClass = "bar-mid";

        html += `
<div class="chart-bar ${barClass}"
style="height:${Math.max(pct, 10)}px"
title="${m.assignment}: ${m.grade}/${m.max}">
</div>`;
    });

    html += `</div></div>`;

    // --------------------------------------------------
    // GRADES
    // --------------------------------------------------

    html += `
<div>

<h2>${activeSubject} Grades</h2>

<table class="terminal-table">

${[...marks].reverse().map(m => `
<tr>
    <td>${m.assignment}</td>
    <td>${m.grade}/${m.max}</td>
</tr>
`).join("")}

</table>

</div>
`;

    // --------------------------------------------------
    // TASKS FULL WIDTH
    // --------------------------------------------------

        let taskHtml = "<ul class='terminal-task-list'>";

    allTasks.forEach(t => {
        // Skip tasks that don't belong to the current subject
        if (t.subject !== activeSubject) return;

        let due = "";
        if (t.due) {
            try {
                due = t.due.toFormat
                    ? t.due.toFormat("dd MMM")
                    : dv.date(t.due).toFormat("dd MMM");
            } catch {}
        }

        taskHtml += `
<li class="${t.completed ? "task-done" : "task-pending"}">
    <span class="task-status">${t.completed ? "✓" : "○"}</span>
    <span class="task-text">${t.text}</span>
    <span class="task-due">${due}</span>
</li>`;
    });

    taskHtml += "</ul>";

    html += `
<div style="grid-column:1/-1;">
<h2>${activeSubject} Tasks</h2>
${taskHtml}
</div>
`;

    html += `</div>`; // close main-grid

    root.innerHTML = html;
}

// ======================================================
// EVENTS
// ======================================================

root.addEventListener("changeSubject", e => {
    activeSubject = e.detail;
    render();
});

render();
```

[[Tasks]]
[[Marks]]
[[Subjects]]