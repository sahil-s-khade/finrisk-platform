import API from "./api";


export const fetchRecentTransactions =
  async (token) => {

    const response = await API.get(

      "/transactions",

      {
        headers: {
          Authorization:
            `Bearer ${token}`
        }
      }
    );

    return response.data;
};

export const fetchFraudExplanation = async (
  payload,
  token
) => {

  const response = await API.post(

    "/explain-fraud",

    payload,

    {
      headers: {
        Authorization: `Bearer ${token}`
      }
    }

  );

  return response.data;
};

// FRAUD ANALYTICS

export const fetchFraudAnalytics = async (token) => {

  const payload = {

    amount: 250000,
    transaction_type: "TRANSFER",
    customer_age: 34,
    account_balance: 500000,
    location: "Mumbai"

  };

  try {

    const response = await API.post(

      "/ensemble-fraud-analysis",

      payload,

      {
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json"
        }
      }

    );

    console.log("FRAUD API RESPONSE:", response.data);

    return response.data;

  } catch (error) {

    console.error(
      "FRAUD API ERROR:",
      error.response?.data || error.message
    );

    throw error;
  }
};