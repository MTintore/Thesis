var chart = c3.generate({
    bindto: '#chart2',
    data: {
      url: '../static/CSV/Chart_data/grades_access.csv?rnd='+(new Date).getTime(),
      x: 'Access_grade',
      type: 'scatter'
    },
    axis: {
      y: {
        label: {
          text: "Average grade",
          position: "outer-middle"
        },
        min: 1,
        max: 9
      },
      x: {
        label: {
          text: "Access grade PAU",
          position: "outer-center"
        },
        min: 9,
        max: 14
      }
    },
    size: {
      height: 400,
      width: 800
    },
    zoom: {
      enabled: true
    },
    legend: {
      show: true,
      position: 'inset',
      inset: {
        anchor: 'top-right',
        x: 20,
        y: 300,
        step: 1
      }
    },

setTimeout(() => {
      var points = chart.data()[0].values.map((d) => [d.x, d.value]),
          slopeIntercept = slopeAndIntercept(points),
          fitPoints = chart.data()[0].values.map((d) => slopeIntercept.slope * d.x + slopeIntercept.intercept);

        chart.load({
          columns: [
            ['Regression'].concat(fitPoints)
          ],
          type: 'line'
        })
    }, 200);

    // simple linear regression
    slopeAndIntercept = function(points) {
      var rV = {},
        N = points.length,
        sumX = 0,
        sumY = 0,
        sumXx = 0,
        sumYy = 0,
        sumXy = 0;

      // can't fit with 0 or 1 point
      if (N < 2) {
        return rV;
      }

      for (var i = 0; i < N; i++) {
        var x = points[i][0],
          y = points[i][1];
        sumX += x;
        sumY += y;
        sumXx += (x * x);
        sumYy += (y * y);
        sumXy += (x * y);
      }

      // calc slope and intercept
      rV['slope'] = ((N * sumXy) - (sumX * sumY)) / (N * sumXx - (sumX * sumX));
      rV['intercept'] = (sumY - rV['slope'] * sumX) / N;
      rV['rSquared'] = Math.abs((rV['slope'] * (sumXy - (sumX * sumY) / N)) / (sumYy - ((sumY * sumY) / N)));

      return rV;
}