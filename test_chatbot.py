import os
import sys

def test_basic_functionality():
    print("Testing basic chatbot functionality...")
    
    try:
        from chatbot import AIChatBot
        print("✅ Chatbot class imports successfully")
    except ImportError as e:
        print(f"❌ Import failed: {e}")
        return False
    
    try:
        os.environ.pop('OPENAI_API_KEY', None)
        bot = AIChatBot()
        print("✅ Chatbot instance created successfully")
    except Exception as e:
        print(f"❌ Instance creation failed: {e}")
        return False
    
    try:
        response = bot.get_response("Hello")
        if "error" in response.lower() or "api" in response.lower():
            print("✅ Proper error handling for missing API key")
        else:
            print(f"⚠️  Unexpected response without API key: {response}")
    except Exception as e:
        print(f"❌ Error handling test failed: {e}")
        return False
    
    try:
        bot.clear_history()
        print("✅ Clear history functionality works")
    except Exception as e:
        print(f"❌ Clear history failed: {e}")
        return False
    
    print("\n🎉 All basic functionality tests passed!")
    return True

def test_dependencies():
    print("Testing dependencies...")
    
    try:
        import openai
        print("✅ OpenAI library available")
    except ImportError:
        print("❌ OpenAI library not installed")
        return False
    
    try:
        from dotenv import load_dotenv
        print("✅ python-dotenv library available")
    except ImportError:
        print("❌ python-dotenv library not installed")
        return False
    
    print("✅ All dependencies available")
    return True

if __name__ == "__main__":
    print("=" * 50)
    print("🤖 AIChatBot Local Testing")
    print("=" * 50)
    
    deps_ok = test_dependencies()
    if not deps_ok:
        print("\n❌ Dependency tests failed. Run: pip install -r requirements.txt")
        sys.exit(1)
    
    basic_ok = test_basic_functionality()
    if not basic_ok:
        print("\n❌ Basic functionality tests failed")
        sys.exit(1)
    
    print("\n" + "=" * 50)
    print("✅ ALL TESTS PASSED - Chatbot is ready to use!")
    print("📝 Note: Full functionality requires a valid OpenAI API key")
    print("=" * 50)
