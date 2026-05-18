import { useState } from "react";

import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";

import {
  fetchFraudExplanation
} from "../services/dashboardService";

function ExplainableAI() {

  const [result, setResult] = useState(null);

  const [loading, setLoading] = useState(false);

  const token = localStorage.getItem("token");

  const samplePayload = {

    amount: 250000,

    transaction_hour: 1,

    is_high_risk_merchant: 1,

    location_risk_score: 98,

    rapid_transaction_flag: 1
  };


  const handleExplain = async () => {

    try {

      setLoading(true);

      const data =
        await fetchFraudExplanation(
          samplePayload,
          token
        );

      console.log(data);

      setResult(data);

    } catch (error) {

      console.error(error);

    } finally {

      setLoading(false);
    }
  };


  return (

    <div className="flex bg-slate-100 min-h-screen">

      <Sidebar />

      <div className="flex-1">

        <Navbar />

        <div className="p-8">

          <div className="bg-gradient-to-r from-indigo-700 to-slate-900 rounded-3xl p-10 text-white shadow-2xl">

            <h1 className="text-5xl font-bold mb-4">

              Explainable AI Engine

            </h1>

            <p className="text-xl text-slate-200">

              AI-powered fraud reasoning
              and transparent ML explanations.

            </p>

          </div>


          <div className="mt-10">

            <button

              onClick={handleExplain}

              className="bg-red-500 hover:bg-red-600 text-white px-8 py-4 rounded-2xl text-xl font-bold shadow-lg transition"

            >

              {loading
                ? "Analyzing..."
                : "Run Fraud Explanation"}

            </button>

          </div>


          {result && (

            <div className="bg-white mt-10 p-10 rounded-3xl shadow-xl">

              <h2 className="text-3xl font-bold mb-8">

                AI Fraud Analysis Result

              </h2>


              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

                {result.explanation
                  ?.top_risk_factors
                  ?.map((factor, index) => (

                  <div

                    key={index}

                    className="bg-slate-50 border border-slate-200 rounded-2xl p-6"

                  >

                    <h3 className="text-2xl font-bold text-red-500 mb-4">

                      {factor.feature}

                    </h3>

                    <p className="text-lg mb-2">

                      Importance:

                      {" "}
                      <span className="font-bold">

                        {factor.importance}

                      </span>

                    </p>

                    <p className="text-lg">

                      Input Value:

                      {" "}
                      <span className="font-bold">

                        {factor.input_value}

                      </span>

                    </p>

                  </div>

                ))}

              </div>

            </div>

          )}

        </div>

      </div>

    </div>
  );
}

export default ExplainableAI;