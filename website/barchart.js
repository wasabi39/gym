// set the dimensions and margins of the graph
        var margin = {top: 20, right: 30, bottom: 40, left: 150},
            width = 600 - margin.left - margin.right,
            height =  500 - margin.top - margin.bottom;
        
        // append the svg object to the body of the page
        var svg = d3.select("#my_dataviz")
          .append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
          .append("g")
            .attr("transform",
                  "translate(" + margin.left + "," + margin.top + ")");
        
        // Parse the Data
        d3.csv("https://raw.githubusercontent.com/wasabi39/gym/main/subject_count_61020_666799.csv", function(data) {
        
          data = data.filter(function (a) { return a.Count >= 10; });

          // sort data
          data.sort(function(b, a) {
            return a.Count - b.Count;
          });
        
          // Add X axis
          var x = d3.scaleLinear()
            .domain([0, 700])
            .range([ 0, width]);
          svg.append("g")
            .attr("transform", "translate(0," + height + ")")
            .call(d3.axisBottom(x))
            .selectAll("text")
              .attr("transform", "translate(-10,0)rotate(-45)")
              .style("text-anchor", "end");

          // Y axis
          var y = d3.scaleBand()
            .range([ 0, height ])
            .domain(data.map(function(d) { return d.Subject; }))
            .padding(.1);
          svg.append("g")
            .call(d3.axisLeft(y))


            
          //Bars

          var div = d3.select("body").append("div")
            .attr("class", "tooltip-bar-chart")
            .style("opacity", 0);
          svg.selectAll("myRect")
            .data(data)
            .enter()
            .append("rect")
            .attr("x", x(0) )
            .attr("y", function(d) { return y(d.Subject); })
            .attr("width", function(d) { return x(d.Count); })
            .attr("height", y.bandwidth() )
            .attr("fill", "#69b3a2")
            //mouse over changes opacity
            .on('mouseover', function (d, i) {
              d3.select(this).transition()
              .duration('50')
              .attr('opacity', '.85')
              div.transition()
               .duration(50)
               .style("opacity", 1);
              let num = d.Subject.charAt(0).toUpperCase() + d.Subject.slice(1) + ": " + d.Count.toString() + " jobopslag";
              div.html(num)
               .style("left", (d3.event.pageX + 10) + "px")
               .style("top", (d3.event.pageY - 15) + "px")
              })

            .on('mouseout', function (d, i) {
              d3.select(this).transition()
              .duration('50')
              .attr('opacity', '1')
              div.transition()
               .duration('50')
               .style("opacity", 0)})


              //.attr("x", function(d) { return x(d.Subject); })
              //.attr("y", function(d) { return y(d.Count); })
              //.attr("width", x.bandwidth())
              //.attr("height", function(d) { return height - y(d.Count); })
              //.attr("fill", "#69b3a2")
        })
