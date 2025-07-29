cat > README.md << 'EOF'
# 🎲 Classroom Cube Engagement System

> Revolutionary interactive learning cubes that transform classroom engagement through AI-powered collaborative activities.

![Build Status](https://github.com/yourusername/classroom-cube-system/workflows/🎲%20Classroom%20Cube%20CI/badge.svg)
![Documentation](https://github.com/yourusername/classroom-cube-system/workflows/📚%20Documentation/badge.svg)

## ✨ Features

- **5-Button Interface**: Simple A, B, C, D corner buttons + center generate button
- **Four Corners Discussions**: AI-generated prompts for position-based debates
- **Multiple Choice Assessments**: Exit tickets, Do Nows, Check for Understanding
- **Real-time Dashboard**: Teacher control and live analytics
- **Mesh Networking**: Reliable cube-to-cube communication
- **Affordable**: ~$168 per cube, $840 for complete 5-cube classroom

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/engage3.git
cd engage3

# Install dependencies
pip install -r requirements.txt

# Set up teacher hub
cd teacher-hub
python main.py

# Set up cube client (on each Raspberry Pi)
cd ../cube-client
python main.py --simulation  # For development without hardware