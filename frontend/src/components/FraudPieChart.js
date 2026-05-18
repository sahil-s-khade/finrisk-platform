import {

  PieChart,

  Pie,

  Cell,

  Tooltip,

  Legend,

  ResponsiveContainer

} from "recharts";


function FraudPieChart({

  fraud,

  normal

}) {

  const data = [

    {
      name: "Fraud",
      value: fraud
    },

    {
      name: "Normal",
      value: normal
    }
  ];


  const COLORS = [

    "#EF4444",

    "#22C55E"
  ];


  return (

    <div className="bg-white p-6 rounded-2xl shadow-lg">

      <h2 className="text-2xl font-bold mb-6">

        Fraud Distribution

      </h2>


      <div className="h-80">

        <ResponsiveContainer>

          <PieChart>

            <Pie

              data={data}

              dataKey="value"

              outerRadius={110}

              label
            >

              {
                data.map((entry, index) => (

                  <Cell

                    key={index}

                    fill={COLORS[index]}
                  />
                ))
              }

            </Pie>

            <Tooltip />

            <Legend />

          </PieChart>

        </ResponsiveContainer>

      </div>

    </div>
  );
}

export default FraudPieChart;