import { useState } from "react";


function LiveTransactions({

  transactions

}) {

  const [filter,
    setFilter] = useState("ALL");


  // FILTER LOGIC
  const filteredTransactions =
    transactions.filter((tx) => {

      if (filter === "SAFE") {

        return !tx.is_fraud;
      }

      if (filter === "FRAUD") {

        return tx.is_fraud;
      }

      return true;
    });


  return (

    <div className="bg-white p-6 rounded-2xl shadow-lg mt-10">

      {/* HEADER */}

      <div className="flex justify-between items-center mb-6">

        <h2 className="text-2xl font-bold">

          Live Fraud Monitoring

        </h2>

        <div className="text-sm text-green-600 font-semibold">

          ● LIVE

        </div>

      </div>


      {/* FILTER BUTTONS */}

      <div className="flex gap-4 mb-6">

        <button

          onClick={() => setFilter("ALL")}

          className={`px-4 py-2 rounded-lg font-semibold ${
            filter === "ALL"
              ? "bg-black text-white"
              : "bg-gray-200"
          }`}
        >

          All

        </button>


        <button

          onClick={() => setFilter("SAFE")}

          className={`px-4 py-2 rounded-lg font-semibold ${
            filter === "SAFE"
              ? "bg-green-500 text-white"
              : "bg-green-100 text-green-700"
          }`}
        >

          Safe

        </button>


        <button

          onClick={() => setFilter("FRAUD")}

          className={`px-4 py-2 rounded-lg font-semibold ${
            filter === "FRAUD"
              ? "bg-red-500 text-white"
              : "bg-red-100 text-red-700"
          }`}
        >

          Fraud

        </button>

      </div>


      {/* TABLE */}

      <div className="overflow-x-auto">

        <table className="w-full">

          <thead>

            <tr className="border-b">

              <th className="text-left py-3">

                Transaction ID

              </th>

              <th className="text-left py-3">

                Amount

              </th>

              <th className="text-left py-3">

                Risk Score

              </th>

              <th className="text-left py-3">

                Status

              </th>

            </tr>

          </thead>


          <tbody>

            {

              filteredTransactions.map((tx) => (

                <tr

                  key={tx.id}

                  className="border-b hover:bg-gray-50"
                >

                  <td className="py-4">

                    {tx.transaction_id}

                  </td>


                  <td className="py-4 font-semibold">

                    ₹ {tx.amount}

                  </td>


                  <td className="py-4">

                    {tx.risk_score}

                  </td>


                  <td className="py-4">

                    {

                      tx.is_fraud ? (

                        <span className="bg-red-100 text-red-600 px-3 py-1 rounded-full text-sm font-semibold">

                          FRAUD

                        </span>

                      ) : (

                        <span className="bg-green-100 text-green-600 px-3 py-1 rounded-full text-sm font-semibold">

                          SAFE

                        </span>
                      )
                    }

                  </td>

                </tr>
              ))
            }

          </tbody>

        </table>

      </div>

    </div>
  );
}

export default LiveTransactions;