<!--TITLE: Feedback &amp; Survey | APU CodeStorm 2026-->
<!--DESC: Post-event feedback survey for APU CodeStorm 2026 participants, volunteers and visitors.-->
<section class="page-header" style="background-image:linear-gradient(rgba(11,18,32,.82),rgba(11,18,32,.92)),url('assets/img/gallery-09.svg')">
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> &rsaquo; Feedback &amp; Survey</p>
    <span class="kicker">2 minutes</span>
    <h1>Feedback &amp; Survey</h1>
    <p class="lead">Tell us what worked, what dragged and what the 2027 edition should fix.</p>
  </div>
</section>

<section class="section">
  <div class="container grid grid--2">
    <div>
      <div class="alert alert--ok">
        <p><strong>Why we ask:</strong> last year&rsquo;s survey moved the mentor clinics to daytime and
          cut the submission queue in half. Your answers are read by the whole committee.</p>
      </div>

      <form data-validate data-success="Thank you - your feedback has been recorded. Results are shared with the committee every Monday." novalidate>
        <div class="form-result alert" hidden role="status"></div>

        <fieldset>
          <legend>1. Overall rating</legend>
          <div class="stars" data-stars role="group" aria-label="Rate your overall experience out of five">
            <button type="button" aria-label="1 star">&#9733;</button>
            <button type="button" aria-label="2 stars">&#9733;</button>
            <button type="button" aria-label="3 stars">&#9733;</button>
            <button type="button" aria-label="4 stars">&#9733;</button>
            <button type="button" aria-label="5 stars">&#9733;</button>
          </div>
          <p id="rating-label" class="muted small">No rating selected</p>
          <input type="hidden" id="rating-value" name="rating" value="0">
        </fieldset>

        <fieldset>
          <legend>2. About you</legend>
          <div class="form-grid">
            <div class="field">
              <label for="frole">Your role <span class="req">*</span></label>
              <select id="frole" name="frole" required>
                <option value="">Select a role</option>
                <option>Competing participant</option>
                <option>Volunteer</option>
                <option>Mentor or judge</option>
                <option>Visitor / audience</option>
              </select>
              <span class="error" aria-live="polite"></span>
            </div>
            <div class="field">
              <label for="ftrack">Track you followed</label>
              <select id="ftrack" name="ftrack">
                <option value="">Not applicable</option>
                <option>01 - AI &amp; Data</option>
                <option>02 - FinTech</option>
                <option>03 - HealthTech</option>
                <option>04 - Sustainability</option>
                <option>05 - Games &amp; XR</option>
                <option>06 - Open Innovation</option>
              </select>
              <span class="error" aria-live="polite"></span>
            </div>
          </div>
        </fieldset>

        <fieldset>
          <legend>3. Your experience</legend>
          <div class="form-grid">
            <div class="field">
              <label for="fcomms">Communication clarity <span class="req">*</span></label>
              <select id="fcomms" name="fcomms" required>
                <option value="">Rate 1&ndash;5</option>
                <option>1 - Hard to follow</option>
                <option>2</option>
                <option>3 - Acceptable</option>
                <option>4</option>
                <option>5 - Excellent</option>
              </select>
              <span class="error" aria-live="polite"></span>
            </div>
            <div class="field">
              <label for="fvenue">Venue &amp; facilities <span class="req">*</span></label>
              <select id="fvenue" name="fvenue" required>
                <option value="">Rate 1&ndash;5</option>
                <option>1 - Poor</option>
                <option>2</option>
                <option>3 - Acceptable</option>
                <option>4</option>
                <option>5 - Excellent</option>
              </select>
              <span class="error" aria-live="polite"></span>
            </div>
            <div class="field">
              <label for="fmentors">Mentor support <span class="req">*</span></label>
              <select id="fmentors" name="fmentors" required>
                <option value="">Rate 1&ndash;5</option>
                <option>1 - Hard to reach</option>
                <option>2</option>
                <option>3 - Acceptable</option>
                <option>4</option>
                <option>5 - Excellent</option>
              </select>
              <span class="error" aria-live="polite"></span>
            </div>
            <div class="field">
              <label for="fjudging">Judging transparency <span class="req">*</span></label>
              <select id="fjudging" name="fjudging" required>
                <option value="">Rate 1&ndash;5</option>
                <option>1 - Opaque</option>
                <option>2</option>
                <option>3 - Acceptable</option>
                <option>4</option>
                <option>5 - Excellent</option>
              </select>
              <span class="error" aria-live="polite"></span>
            </div>
          </div>
        </fieldset>

        <fieldset>
          <legend>4. Open comments</legend>
          <div class="form-grid">
            <div class="field field--full">
              <label for="fbest">What worked best?</label>
              <textarea id="fbest" name="fbest" rows="3" placeholder="Mentor clinics, the venue, the pacing..."></textarea>
              <span class="error" aria-live="polite"></span>
            </div>
            <div class="field field--full">
              <label for="fworst">What should we change? <span class="req">*</span></label>
              <textarea id="fworst" name="fworst" rows="3" minlength="10" required
                        placeholder="Be specific - even small annoyances help."></textarea>
              <span class="error" aria-live="polite"></span>
            </div>
            <div class="field field--full">
              <label class="check">
                <input type="checkbox" id="fcontact" name="fcontact">
                The committee may contact me about this feedback.
              </label>
            </div>
          </div>
        </fieldset>

        <button class="btn btn--block" type="submit">Submit feedback</button>
        <p class="form-note">Responses are anonymised unless you tick the contact box.</p>
      </form>
    </div>

    <aside>
      <div class="panel">
        <h3>Survey snapshot</h3>
        <p class="muted small">From the imaginary 2025 edition (212 responses)</p>
        <p>Overall satisfaction <strong>4.4 / 5</strong></p>
        <div class="progress" role="img" aria-label="Overall satisfaction 4.4 out of 5"><span style="width:88%"></span></div>
        <p style="margin-top:.9rem">Would participate again <strong>91%</strong></p>
        <div class="progress" role="img" aria-label="Would participate again 91 percent"><span style="width:91%"></span></div>
        <p style="margin-top:.9rem">Found a team easily <strong>78%</strong></p>
        <div class="progress" role="img" aria-label="Found a team easily 78 percent"><span style="width:78%"></span></div>
      </div>

      <div class="panel" style="margin-top:1.2rem">
        <h3>What we changed since</h3>
        <ul>
          <li>Mentor clinics moved before midnight.</li>
          <li>Second submission server added for the Sunday rush.</li>
          <li>Quiet room relocated away from the build floor.</li>
          <li>Track briefs published two weeks earlier.</li>
        </ul>
      </div>

      <div class="card" style="margin-top:1.2rem">
        <h3>Prefer a conversation?</h3>
        <p>Drop by the feedback booth next to the registration desk, or send the committee a message.</p>
        <p><a href="contact.html">Contact the committee &rarr;</a></p>
      </div>
    </aside>
  </div>
</section>
