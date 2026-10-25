# Hotel Booking Cancellation Dashboard

## 1. Decision-maker and decision

This dashboard is for a **hotel revenue manager** who must decide **how to adjust room inventory and deposit requirements across market segments**. The manager can filter by hotel type and market segment, then compare cancellation rates, prices, booking volume, and monthly patterns before changing a segment's allocation or payment policy.

The dashboard is descriptive: it helps identify where cancellations are concentrated, but it does not by itself prove that a deposit policy or inventory change will reduce cancellations.

## 2. Data and preparation

- **Source:** Kaggle, *Hotel Booking Demand*, file `hotel_bookings.csv`.
- **Coverage:** the Kaggle snapshot covers arrivals from July 2015 to August 2017.
- **Unit of analysis:** one hotel booking.
- **Cleaning:** records with negative ADR or ADR of at least €1,000 are removed because they are data errors or extreme outliers that would distort the average. A valid arrival date is constructed from the arrival year, month, and day for the monthly chart.
- **Important limitation:** this is an old historical snapshot, not live hotel performance. Missing `children`, `company`, and `agent` fields remain in the source data but are not used in the displayed metrics.

## 3. What is shown, and why

The top of the page contains only three headline measures:

1. **Cancellation rate** — the main problem the manager needs to control.
2. **Average daily rate (ADR)** — shows the revenue context behind a cancellation decision.
3. **Booking count** — prevents a high cancellation rate in a very small segment from being mistaken for a large business problem.

Two supporting views explain the headline numbers:

- **Monthly cancellation-rate trend:** reveals seasonality and shows whether a high overall rate is concentrated in particular arrival months.
- **Cancellation rate by market segment:** identifies the channels or customer segments that may need different inventory or deposit rules.

The two filters match the manager's decision. Hotel type separates City Hotel and Resort Hotel because their demand patterns differ; market segment isolates the channels for which the manager can change allocations or policies. A small detail table supports spot checks without dominating the page.

## 4. What was cut, and why

I did not put every source column on the dashboard. Country, customer type, room assignment, parking requests, special requests, agent, and company were left out of the main view because they do not directly answer the selected allocation-and-deposit question. I also avoided a large set of filters and additional KPI cards: they would make the page slower to interpret and encourage comparisons based on very small groups. The raw table is limited to the first 500 filtered rows and is hidden in an expander.

## 5. Refresh and review cadence

The submitted app uses a static Kaggle file, so its contents do not change unless the CSV is replaced. In a production hotel system, the underlying booking data should be **refreshed daily**, because new bookings and cancellations arrive continuously. The revenue manager should **review the dashboard weekly**, before the regular allocation and rate review, and investigate any segment whose weekly cancellation rate is more than 15% above its own historical average. That threshold is a proposed monitoring rule, not an alert implemented in this classroom app.

## Run locally

Place `hotel_bookings.csv` in the repository root, next to `app.py`, then run:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy with Streamlit Community Cloud

Push `app.py`, `requirements.txt`, `README.md`, and `hotel_bookings.csv` to your own GitHub repository. In your own Streamlit Community Cloud account, choose that repository and set the main file path to `app.py`.
