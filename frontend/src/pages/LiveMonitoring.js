import { useEffect, useState } from "react";

import Sidebar from "../components/Sidebar";

import Navbar from "../components/Navbar";

import LiveTransactions from "../components/LiveTransactions";

import {
  fetchRecentTransactions
} from "../services/dashboardService";


function LiveMonitoring() {

  const [transactions,
    setTransactions] = useState([]);

  const [loading,
    setLoading] = useState(true);


  const token =
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc3OTA5MzA0MCwianRpIjoiZjIyMzExYjQtOTZmMS00YzIwLTk5YzItMTNjMTcxNjdlYTk4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImFkbWluIiwibmJmIjoxNzc5MDkzMDQwLCJjc3JmIjoiOWEwM2E4MjAtMTEwNi00MWE0LWIzNTYtMGM2ZDNlZTA1ODZkIiwiZXhwIjoxNzc5MDkzOTQwfQ.o67zpn5ibKEbkqrWiGxNXQ81VIeKms4Wtif1hDxeyhQ";


  useEffect(() => {

    const loadTransactions =
      async () => {

      try {

        const txData =
          await fetchRecentTransactions(token);

        if (Array.isArray(txData)) {

          setTransactions(txData);

        } else if (
          txData.transactions
        ) {

          setTransactions(
            txData.transactions
          );
        }

      } catch (error) {

        console.error(error);

      } finally {

        setLoading(false);
      }
    };

    loadTransactions();

  }, [token]);


  if (loading) {

    return (

      <div className="p-10 text-3xl">

        Loading Transactions...

      </div>
    );
  }


  return (

    <div className="flex bg-gray-100 min-h-screen">

      <Sidebar />

      <div className="flex-1">

        <Navbar />

        <div className="p-8">

          <h1 className="text-4xl font-bold mb-8">

            Live Fraud Monitoring

          </h1>

          <LiveTransactions
            transactions={transactions}
          />

        </div>

      </div>

    </div>
  );
}

export default LiveMonitoring;