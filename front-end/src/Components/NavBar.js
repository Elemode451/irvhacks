import React from 'react';
import { Link } from 'react-router-dom';

const NavBar = () => {
  return (
    <nav className="bg-[#121212] text-white py-[20px] pl-6 font-mono">
      <ul className="flex space-x-[112px]">
        <li>
            <Link to="/" className="p-0 bg-transparent border-0 focus:outline-none hover:opacity-80">
                <img
                src="/real_home_button.png"
                alt="Patient Logo"
                className="w-8 h-8 " // Adjust size as needed
                />
            </Link>
        </li>
        <li>
          <Link to="/search" className="hover:text-gray-400 hover:underline text-xl">Search</Link>
        </li>
        <li>
          <Link to="/contact-us" className="hover:text-gray-400 hover:underline text-xl">Contact Us</Link>
        </li>
        <li>
          <Link to="/about" className="hover:text-gray-400 hover:underline text-xl">About Us</Link>
        </li>
      </ul>
    </nav>
  );
};

export default NavBar;
