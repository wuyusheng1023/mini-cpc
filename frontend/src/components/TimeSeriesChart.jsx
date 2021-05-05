import React from "react";
import { TimeSeries, Index } from "pondjs";
import { Charts, ChartContainer, ChartRow, YAxis, LineChart} from "react-timeseries-charts";

const values =  [
    ["2017-01-24T00:00", 1000],
    ["2017-01-24T01:00", 1100],
    ["2017-01-24T02:00", 1400],
  ];

export default function TimeSeriesChart({data}) {

  const n = 60;

  const series = new TimeSeries({
    name: "hilo_rainfall",
    columns: ["index", "conc"],
    points: values.map(([d, v]) => [Index.getIndexString("1min", new Date(d)),v])
  });

  return (
    <ChartContainer timeRange={series.range()} width={500}>
      <ChartRow height="350">
        <YAxis
          id="axis1"
          label="Number Concentration (#/cm^3)"
          min={900}
          max={1500}
          format=".2f"
          width="70"
          type="linear"
        />
        <Charts>
          <LineChart
            axis="axis1"
            columns={["conc"]}
            series={series}
          />
        </Charts>
      </ChartRow>
    </ChartContainer>
  );
};
