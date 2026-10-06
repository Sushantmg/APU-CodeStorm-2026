<!--TITLE: Participant Login | APU CodeStorm 2026-->
<!--DESC: Sign in to the APU CodeStorm 2026 participant dashboard to manage your team, schedule and submissions.-->
<section class="page-header" style="background-image:linear-gradient(rgba(11,18,32,.82),rgba(11,18,32,.92)),url('assets/img/register-banner.svg')">
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> &rsaquo; Login</p>
    <span class="kicker">Participants only</span>
    <h1>Participant Login</h1>
    <p class="lead">Access your team profile, personalised schedule and submission portal.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="panel login-card">
      <div class="avatar-preview" aria-hidden="true">&#128104;&#8205;&#128187;</div>
      <h2 class="text-center" style="font-size:1.4rem">Sign in</h2>
      <p class="muted small text-center">Use the e-mail address you registered with.</p>

      <form id="login-form" novalidate>
        <div class="form-result alert" hidden role="status"></div>

        <div class="field">
          <label for="login-email">E-mail <span class="req">*</span></label>
          <input id="login-email" name="login-email" type="email" autocomplete="username" required
                 placeholder="you@student.apu.edu.my">
        </div>

        <div class="field" style="margin-top:.9rem">
          <label for="login-password">Password <span class="req">*</span></label>
          <input id="login-password" name="login-password" type="password"
                 autocomplete="current-password" minlength="4" required placeholder="Minimum 4 characters">
        </div>

        <div class="field" style="margin-top:.9rem">
          <label class="check"><input type="checkbox" id="remember" name="remember"> Keep me signed in on this device</label>
        </div>

        <button class="btn btn--block" type="submit" style="margin-top:1.1rem">Sign in</button>
        <p class="form-note text-center" style="margin-top:.8rem">
          <a href="contact.html">Forgot your password?</a>
        </p>
      </form>

      <hr style="border:0;border-top:1px solid var(--border);margin:1.4rem 0">

      <p class="small muted text-center">This is a front-end demonstration: any valid e-mail and a
        password of four or more characters will open the dashboard. Nothing is sent to a server.</p>
      <p class="text-center"><a class="btn btn--ghost" href="register.html">Create an account instead</a></p>
    </div>

    <div class="grid grid--3" style="margin-top:2rem">
      <article class="card">
        <h3>Your schedule</h3>
        <p>A personalised view of the sessions your team booked, plus mentor office-hour slots.</p>
      </article>
      <article class="card">
        <h3>Submissions</h3>
        <p>Upload the repository link, build log, slide deck and demo video before the code freeze.</p>
      </article>
      <article class="card">
        <h3>Score sheets</h3>
        <p>After demo day, your judges' written feedback appears here within five working days.</p>
      </article>
    </div>
  </div>
</section>
