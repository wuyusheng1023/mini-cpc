import Plot from 'react-plotly.js';


export default function TimeSeriesChart({ dataArr }) {

  const x = dataArr.map(v => v['datetime']);
  const y = dataArr.map(v => v['concentration']);

  return (
    <Plot
      data={[
        {
          x: x,
          y: y,
        },
        { type: 'scatter' },
      ]}
      layout={{
        width: 520,
        height: 400,
        yaxis: {
          title: 'Number Concentraion (#/cm3)',
        },
      }}
    />
  );
};
