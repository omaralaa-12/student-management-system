import { useState } from "react";
import api from "../services/api";

function AIChat() {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  async function askAI() {
    if (!question.trim()) return;

    const userMessage = {
      sender: "user",
      text: question,
    };

    setMessages((prev) => [...prev, userMessage]);

    setLoading(true);

    try {
      const response = await api.post("/ai/chat", {
        question,
      });

      const aiMessage = {
        sender: "ai",
        text: response.data.answer,
      };

      setMessages((prev) => [...prev, aiMessage]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          sender: "ai",
          text: "Something went wrong.",
        },
      ]);
    }

    setQuestion("");
    setLoading(false);
  }

  return (
    <div className="bg-white rounded-lg shadow p-6 mt-8">

      <h2 className="text-2xl font-bold mb-4">
        🤖 AI Assistant
      </h2>

      <div className="border rounded p-4 h-96 overflow-y-auto bg-gray-50">

        {messages.length === 0 && (
          <p className="text-gray-500">
            Ask anything about your students...
          </p>
        )}

        {messages.map((msg, index) => (

          <div
            key={index}
            className={`mb-4 ${
              msg.sender === "user"
                ? "text-right"
                : "text-left"
            }`}
          >

            <span
              className={`inline-block px-4 py-3 rounded-lg max-w-xl ${
                msg.sender === "user"
                  ? "bg-blue-600 text-white"
                  : "bg-gray-200"
              }`}
            >
              {msg.text}
            </span>

          </div>

        ))}

        {loading && (
          <p className="text-gray-500">
            AI is thinking...
          </p>
        )}

      </div>

      <div className="flex mt-4">

        <input
          className="flex-1 border rounded-l p-3"
          placeholder="Ask a question..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              askAI();
            }
          }}
        />

        <button
          onClick={askAI}
          className="bg-green-600 text-white px-6 rounded-r hover:bg-green-700"
        >
          Send
        </button>

      </div>

    </div>
  );
}

export default AIChat;