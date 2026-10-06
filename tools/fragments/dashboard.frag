<!--TITLE: Participant Dashboard | APU CodeStorm 2026-->
<!--DESC: Personalised dashboard for APU CodeStorm 2026 participants - team profile, schedule, submissions and downloads.-->
<section class="page-header" style="background-image:linear-gradient(rgba(11,18,32,.82),rgba(11,18,32,.92)),url('assets/img/gallery-04.svg')">
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> &rsaquo; Dashboard</p>
    <span class="kicker">Personal hub</span>
    <h1>Welcome back, <span id="dash-user">Guest Hacker</span></h1>
    <p class="lead">Everything your team needs before, during and after the 48 hours.</p>
    <div class="btn-row">
      <a class="btn btn--ghost" href="schedule.html">Full programme</a>
      <button class="btn btn--ghost" id="logout-btn" type="button">Sign out</button>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="kicker">At a glance</span>
      <h2>Team status</h2>
    </div>

    <div class="dashboard-grid">
      <div class="panel">
        <h3><span aria-hidden="true">&#127919;</span> Team profile</h3>
        <ul>
          <li>Team: <strong>Null Pointers</strong></li>
          <li>Track: <strong>01 - AI &amp; Data</strong></li>
          <li>Members: <strong>4 of 4 confirmed</strong></li>
          <li>Team code: <strong>CS26-NP-0417</strong></li>
        </ul>
        <p class="small"><a href="register.html">Edit roster &rarr;</a></p>
      </div>

      <div class="panel">
        <h3><span aria-hidden="true">&#128197;</span> Your next sessions</h3>
        <ul>
          <li><strong>Fri 09:00</strong> - Opening ceremony (LT1)</li>
          <li><strong>Fri 14:00</strong> - Architecture clinic (Lab)</li>
          <li><strong>Sat 10:00</strong> - UX clinic (Lab)</li>
          <li><strong>Sun 14:00</strong> - Demo day pitch (LT1)</li>
        </ul>
        <p class="small"><a href="schedule.html">See the full schedule &rarr;</a></p>
      </div>

      <div class="panel">
        <h3><span aria-hidden="true">&#9997;</span> Submission progress</h3>
        <p class="muted small">2 of 4 items complete</p>
        <div class="progress" role="img" aria-label="Submission progress 50 percent"><span style="width:50%"></span></div>
        <ul style="margin-top:.8rem">
          <li>&#10003; Team roster confirmed</li>
          <li>&#10003; Track selection locked</li>
          <li>&#9675; Repository link</li>
          <li>&#9675; Demo video (max 200 MB)</li>
        </ul>
      </div>

      <div class="panel">
        <h3><span aria-hidden="true">&#9200;</span> Countdown to code freeze</h3>
        <div class="countdown" data-countdown="2026-12-06T12:00:00+08:00" aria-label="Countdown to the code freeze">
          <div><b data-unit="days">00</b><span>Days</span></div>
          <div><b data-unit="hours">00</b><span>Hours</span></div>
          <div><b data-unit="minutes">00</b><span>Minutes</span></div>
          <div><b data-unit="seconds">00</b><span>Seconds</span></div>
        </div>
        <p class="small muted" style="margin-top:.8rem">Sunday 6 December 2026, 12:00 (GMT+8).</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section-head">
      <span class="kicker">Personalised feed</span>
      <h2>Announcements for your track</h2>
    </div>

    <div class="dashboard-grid">
      <div class="panel">
        <span class="badge badge--danger">Action needed</span>
        <h3 style="margin-top:.7rem">Upload your repository link</h3>
        <p class="muted small">Due before the code freeze on 6 December, 12:00. The build log must be
          committed with the code.</p>
        <p><a class="btn btn--ghost" href="resources.html">Get the build log template</a></p>
      </div>

      <div class="panel">
        <span class="badge">Mentor slot</span>
        <h3 style="margin-top:.7rem">Dr. Wong - AI architecture</h3>
        <p class="muted small">Saturday 5 December, 11:00&ndash;11:20, Mentor Desk 3. Bring your data model
          sketch.</p>
        <p><a href="schedule.html">View clinic hours &rarr;</a></p>
      </div>

      <div class="panel">
        <span class="badge badge--accent">Reminder</span>
        <h3 style="margin-top:.7rem">Pitch rehearsal slots</h3>
        <p class="muted small">Sunday 12:30&ndash;13:30 in Seminar Room 2. Two slots left for track 01.</p>
        <p><a href="contact.html">Reserve a slot &rarr;</a></p>
      </div>
    </div>

    <div class="grid grid--2" style="margin-top:1.6rem">
      <div class="panel">
        <h3>Quick downloads</h3>
        <ul class="download-list">
          <li><span><strong>Judging rubric</strong><br><span class="meta">All six tracks &middot; TXT</span></span>
            <a class="btn btn--ghost" href="resources.html">Open library</a></li>
          <li><span><strong>Programme (.ics)</strong><br><span class="meta">Sync every session to your calendar</span></span>
            <a class="btn btn--ghost" href="schedule.html">Schedule page</a></li>
          <li><span><strong>Design kit</strong><br><span class="meta">Logo, colours, icons &middot; SVG</span></span>
            <a class="btn btn--ghost" href="assets/img/logo.svg">Download</a></li>
        </ul>
      </div>

      <div class="panel">
        <h3>Score sheets</h3>
        <p class="muted small">Nothing to show yet. Written feedback from the judging panel appears here
          within five working days of demo day.</p>
        <div class="progress" role="img" aria-label="Score sheets pending"><span style="width:6%"></span></div>
        <p class="small" style="margin-top:.9rem"><a href="activities.html">Review the rubric before
          judging &rarr;</a></p>
      </div>
    </div>
  </div>
</section>
