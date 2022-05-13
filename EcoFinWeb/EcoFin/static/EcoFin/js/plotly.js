function genrateGraph(data,plotId,typeOfGraph,orientationType) {

    var xValues = [];
    var yValues = [];
    data = data[1];
    data.forEach(genratedData);

    function genratedData(item, index) {
      let date = new Date(item.date);
      if (item.value != null) {
        xValues.push(date);
        yValues.push(item.value);
      }
    }

    var dataPlot = [
      {
        x: xValues,
        y: yValues,
        type: typeOfGraph,
        orientation: orientationType
      },
    ];

    var layout = {
      xaxis: {
        type: "date",
        title: "Years",
        ticks: "outside",
        tick0: 0,
        dtick: "M12",
      },
      yaxis: {
        title: "Values",
      },
      title: "Time vs Value",
    };

    const config = {
      displayModeBar: false, // this is the line that hides the bar.
    };

    Plotly.newPlot(plotId, dataPlot, layout, config);
  }